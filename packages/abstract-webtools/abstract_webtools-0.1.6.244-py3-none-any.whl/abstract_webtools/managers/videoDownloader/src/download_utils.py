from .imports import *
from .path_utils import *
_LOCK = threading.RLock()
# ---------------- Registry ---------------- #

class infoRegistry(metaclass=SingletonMeta):
    """Thread-safe registry with all video assets stored under ~/videos/<video_id>/ or flat."""

    def __init__(self, video_root=None, flat_layout: bool = False, **kwargs):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.video_root = get_video_root(video_root)
            self.flat_layout = flat_layout
            self.registry_path = os.path.join(self.video_root, "registry.json")
            self._load_registry()


    def _load_registry(self):
        with _LOCK:
            self.registry = {"by_url": {}, "by_id": {}, "by_path": {}}
            if os.path.isfile(self.registry_path):
                try:
                    with open(self.registry_path, "r", encoding="utf-8") as f:
                        j = json.load(f)
                    self.registry["by_url"].update(j.get("by_url", {}))
                    self.registry["by_id"].update(j.get("by_id", {}))
                    self.registry["by_path"].update(j.get("by_path", {}))
                except Exception:
                    pass

    def _save_registry(self):
        with _LOCK:
            get_atomic_write(self.registry_path, self.registry)

    # ---------- pruning ----------

    def prune_registry(self, dry_run: bool = False):
        """Remove broken .NA / recommended / missing-path entries."""
        removed = []
        with _LOCK:
            to_delete = []
            for vid, meta in self.registry["by_id"].items():
                vpath = meta.get("video_path")
                url = meta.get("url", "")
                if not vpath or vpath.endswith(".NA") or not os.path.exists(vpath):
                    to_delete.append(vid)
                if url.endswith("/watch") and "v=" not in url:
                    to_delete.append(vid)
            for vid in set(to_delete):
                removed.append(vid)
                self.registry["by_id"].pop(vid, None)
                self.registry["by_url"] = {u: v for u, v in self.registry["by_url"].items() if v != vid}
                self.registry["by_path"] = {p: v for p, v in self.registry["by_path"].items() if v != vid}
            if not dry_run:
                self._save_registry()
        if removed:
            logger.info(f"[infoRegistry] Pruned {len(removed)} invalid entries: {removed}")
        return removed

    # ---------- cache helpers ----------


    def _read_cached_info(self, video_id: str) -> dict | None:
        cache_dir = self.video_root if self.flat_layout else os.path.join(self.video_root, video_id)
        cache = os.path.join(cache_dir, "info.json")
        if os.path.isfile(cache):
            try:
                with open(cache, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return None
        return None

    def _write_cached_info(self, video_id: str, info: dict) -> str:
        cache_dir = self.video_root if self.flat_layout else os.path.join(self.video_root, video_id)
        os.makedirs(cache_dir, exist_ok=True)
        cache = os.path.join(cache_dir, "info.json")
        get_atomic_write(cache, info)
        return cache

    def _resolve_video_id(self, url: str | None, video_path: str | None, hint_id: str | None) -> str | None:
        if hint_id:
            return hint_id
        if video_path and video_path in self.registry["by_path"]:
            return self.registry["by_path"][video_path]
        if url and url in self.registry["by_url"]:
            return self.registry["by_url"][url]
        return None

    def _link(self, video_id: str, url: str | None, video_path: str | None):
        with _LOCK:
            if url:
                self.registry["by_url"][url] = video_id
            if video_path:
                self.registry["by_path"][video_path] = video_id
            rec = self.registry["by_id"].get(video_id, {})
            if url:
                rec["url"] = url
            if video_path:
                rec["video_path"] = video_path
            rec["timestamp"] = time.time()
            self.registry["by_id"][video_id] = rec
            self._save_registry()

    # ---------- main API ----------

    def get_video_info(self, url: str | None = None, video_id: str | None = None,
                       force_refresh: bool = False, video_path: str | None = None) -> dict | None:
        # prune each call
        self.prune_registry(dry_run=False)

        # reject bare /watch
        if url and "youtube.com/watch" in url and "v=" not in url:
            logger.debug(f"[infoRegistry] Ignoring bare watch URL: {url}")
            return None

        if video_path and os.path.isfile(video_path):
            vid = video_id or generate_video_id(video_path)
            info = make_video_info(video_path)
            cache = self._write_cached_info(vid, info)
            self._link(vid, url, os.path.abspath(video_path))
            info["info_path"] = cache
            info["video_id"] = vid
            return ensure_standard_paths(info, self.video_root)

        vid = self._resolve_video_id(url, video_path, video_id)

        if vid and not force_refresh:
            cached = self._read_cached_info(vid)
            if cached:
                self._link(vid, url, cached.get("file_path"))
                cached["info_path"] = os.path.join(self.video_root, vid, "info.json")
                cached["video_id"] = vid
                return ensure_standard_paths(cached, self.video_root)

        if url:
            info = get_yt_dlp_info(url)
            if info:
                vid = info.get("id") or get_sha12(url)
                cache = self._write_cached_info(vid, info)
                self._link(vid, url, None)
                info["info_path"] = cache
                info["video_id"] = vid
                return ensure_standard_paths(info, self.video_root)

        return None

    def edit_info(self, data: dict, url: str | None = None,
                  video_id: str | None = None, video_path: str | None = None):
        cur = self.get_video_info(url=url, video_id=video_id, video_path=video_path, force_refresh=False)
        if not cur:
            raise RuntimeError("No existing info to edit")
        cur.update(data or {})
        vid = cur.get("video_id") or video_id or (url and get_sha12(url)) or generate_video_id(video_path or "video")
        cur = ensure_standard_paths(cur, self.video_root)
        cache = self._write_cached_info(vid, cur)
        self._link(vid, url, cur.get("file_path") or video_path)
        cur["info_path"] = cache
        cur["video_id"] = vid
        return cur

    def list_cached_videos(self):
        with _LOCK:
            return [
                {"video_id": vid, "url": meta.get("url"),
                 "video_path": meta.get("video_path"), "timestamp": meta.get("timestamp")}
                for vid, meta in self.registry["by_id"].items()
            ]


# ---------------- Downloader ---------------- #

class VideoDownloader:
    def __init__(self, url, download_directory=None, user_agent=None,
                 video_extention="mp4", download_video=True,
                 output_filename=None, ydl_opts=None,
                 registry=None, force_refresh=False,
                 flat_layout: bool = False):

        self.url = get_corrected_url(url=url)
        self.video_urls = self.url if isinstance(self.url, list) else [self.url]

        self.registry = registry or infoRegistry(video_root=download_directory,
                                                 flat_layout=flat_layout)
        self.ydl_opts = ydl_opts or {}
        self.get_download = download_video
        self.user_agent = user_agent
        self.video_extention = video_extention
        self.download_directory = get_video_root(download_directory)
        self.output_filename = output_filename
        self.force_refresh = force_refresh
        self.flat_layout = flat_layout   # 🔑

        self.monitoring = True
        self.pause_event = threading.Event()

        self._start()

    def _start(self):
        self.download_thread = threading.Thread(
            target=self._download_entrypoint, name="video-download", daemon=True
        )
        self.monitor_thread = threading.Thread(
            target=self._monitor, name="video-monitor", daemon=True
        )
        self.download_thread.start()
        self.monitor_thread.start()
        self.download_thread.join()

    def stop(self):
        self.monitoring = False
        self.pause_event.set()

    def _monitor(self, interval=30, max_minutes=15):
        start = time.time()
        while self.monitoring:
            logger.info("Monitoring...")
            if time.time() - start > max_minutes * 60:
                logger.info("Monitor: timeout reached, stopping.")
                break
            self.pause_event.wait(interval)
        logger.info("Monitor: exited.")

    def _build_ydl_opts(self, outtmpl, extractor_client=None):
        fmt = "bestvideo+bestaudio/best"
        if self.video_extention and self.video_extention != "mp4":
            fmt = f"bestvideo[ext={self.video_extention}]+bestaudio[ext=m4a]/best[ext={self.video_extention}]"

        opts = {
            "quiet": True,
            "noprogress": True,
            "external_downloader": "ffmpeg",
            "outtmpl": outtmpl,
            "format": fmt,
            "merge_output_format": "mp4",
            "concurrent_fragment_downloads": 3,
            "retries": 5,
            "fragment_retries": 5,
            "ignoreerrors": False,
        }
        if extractor_client:
            opts.setdefault("extractor_args", {}).setdefault("youtube", {})["player_client"] = [extractor_client]
        if self.user_agent:
            opts["http_headers"] = {"User-Agent": self.user_agent}
        opts.update(self.ydl_opts)
        return opts

    def _download_entrypoint(self):
        try:
            for url in self.video_urls:
                self._download_single(url)
        finally:
            self.stop()

    def _download_single(self, video_url: str):
        logger.info(f"[VideoDownloader] Processing: {video_url}")

        if "youtube.com/watch" in video_url and "v=" not in video_url:
            logger.debug(f"[VideoDownloader] Skipping bare watch URL: {video_url}")
            return None

        info = self.registry.get_video_info(url=video_url, force_refresh=self.force_refresh)
        if info and info.get("video_path") and os.path.isfile(info["video_path"]):
            logger.info(f"[VideoDownloader] Already cached: {info['video_path']}")
            return info

        try:
            outtmpl = os.path.join(self.download_directory, "%(id)s.%(ext)s")
            with yt_dlp.YoutubeDL(self._build_ydl_opts(outtmpl)) as ydl:
                raw_info = ydl.extract_info(video_url, download=self.get_download)

            video_id = raw_info.get("id") or generate_video_id(raw_info.get("title") or "video")

            # 🔑 flat or nested
            dirbase = self.download_directory if self.flat_layout else os.path.join(self.download_directory, video_id)
            os.makedirs(dirbase, exist_ok=True)

            temp_path = ydl.prepare_filename(raw_info)
            _, ext = os.path.splitext(temp_path)
            ext = (ext.lstrip(".") or raw_info.get("ext") or "mp4").lower()
            if not re.match(r"^[a-z0-9]+$", ext):
                logger.warning(f"[VideoDownloader] Invalid ext {ext}, forcing mp4")
                ext = "mp4"

            final_path = os.path.join(dirbase, f"video.{ext}")
            if temp_path != final_path and os.path.isfile(temp_path):
                shutil.move(temp_path, final_path)

            minimal_info = {
                "id": raw_info.get("id"),
                "title": raw_info.get("title"),
                "ext": ext,
                "duration": raw_info.get("duration"),
                "upload_date": raw_info.get("upload_date"),
                "video_id": video_id,
                "video_path": final_path,
                "file_path": final_path,
            }
            self.registry.edit_info(minimal_info, url=video_url,
                                    video_id=video_id, video_path=final_path)

            info = self.registry.get_video_info(video_id=video_id)
            logger.info(f"[VideoDownloader] Stored in registry at {info['video_path']}")
            return info

        except Exception as e:
            logger.error(f"[VideoDownloader] Download failed: {e}")
            return None
def get_registryManager(
    video_directory=None,
    envPath=None,
    info_directory=None
    ):
    return infoRegistry(video_directory=video_directory, envPath=envPath, info_directory=info_directory)
def get_video_info(
    url=None,
    video_id=None,
    force_refresh=False,
    video_directory=None,
    envPath=None,
    info_directory=None,
    video_path=None,
    video_url=None,
    download=False
    ):
    url = url or video_url
    registryMgr = get_registryManager(video_directory=video_directory, envPath=envPath, info_directory=info_directory)
    return registryMgr.get_video_info(url=url, video_id=video_id, force_refresh=force_refresh,video_path=video_path)
def get_video_info_spec(
    key=None,
    url=None,
    video_id=None,
    force_refresh=False,
    video_directory=None,
    envPath=None,
    info_directory=None,
    video_path=None,
    video_url=None,
    download=None
    ):
    url = url or video_url
    video_info = get_video_info(
        url=url,
        video_id=video_id,
        force_refresh=force_refresh,
        video_directory=video_directory,
        envPath=envPath,
        info_directory=info_directory,
        video_path=video_path,
        download=download

    )
    if not key:
        return video_info
    value = video_info.get(key)
    if not value:
         value = make_list(get_any_value(video_info,key) or None)[0]
    return value
def get_video_id(
    url=None,
    video_id=None,
    force_refresh=False,
    video_directory=None,
    envPath=None,
    info_directory=None,
    video_path=None,
    video_url=None,
    download=False
    ):
    url = url or video_url
    if download:
        VideoDownloader(url=url)
    return get_video_info_spec(
        key='id',
        url=url,
        video_id=video_id,
        force_refresh=force_refresh,
        video_directory=video_directory,
        envPath=envPath,
        info_directory=info_directory,
        video_path=video_path,
        download=download,
        
        )
def get_video_title(
    url=None,
    video_id=None,
    force_refresh=False,
    video_directory=None,
    envPath=None,
    info_directory=None,
    video_path=None,
    video_url=None,
    download=False
    
    ):
    url = url or video_url
    if download:
        VideoDownloader(url=url)
    return get_video_info_spec(
        key='title',
        url=url,
        video_id=video_id,
        force_refresh=force_refresh,
        video_directory=video_directory,
        envPath=envPath,
        info_directory=info_directory,
        video_path=video_path,
        download=download
        )
def get_video_filepath(
    url=None,
    video_id=None,
    force_refresh=False,
    video_directory=None,
    envPath=None,
    info_directory=None,
    video_path=None,
    video_url=None,
    download=False
    
    ):
    url = url or video_url
    if download:
        VideoDownloader(url=url)
    return get_video_info_spec(
        key='filepath',
        url=url,
        video_id=video_id,
        force_refresh=force_refresh,
        video_directory=video_directory,
        envPath=envPath,
        info_directory=info_directory,
        video_path=video_path,
        download=download
        )
def get_temp_id(url):
    url = str(url)
    url_length = len(url)
    len_neg = 20
    len_neg = len_neg if url_length >= len_neg else url_length
    temp_id = re.sub(r'[^\w\d.-]', '_', url)[-len_neg:]
    return temp_id
def get_temp_file_name(url):
    temp_id = get_temp_id(url)
    temp_filename = f"temp_{temp_id}.mp4"
    return temp_filename
def get_display_id(info):
    display_id = info.get('display_id') or info.get('id')
    return display_id

def get_safe_title(title):
    re_str = r'[^\w\d.-]'
    safe_title = re.sub(re_str, '_', title)
    return safe_title
def get_video_info_from_mgr(video_mgr):
    try:
        info = video_mgr.info
        return info
    except Exception as e:
        print(f"{e}")
        return None
