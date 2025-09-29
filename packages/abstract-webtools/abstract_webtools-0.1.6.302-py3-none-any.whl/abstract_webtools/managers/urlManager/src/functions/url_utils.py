import threading,os,re,yt_dlp
EXTENTIONS=['.ac', '.academy', '.accountant', '.actor', '.agency', '.ai', '.airforce', '.am',
            '.apartments', '.archi', '.army', '.art', '.asia', '.associates', '.at', '.attorney',
            '.auction', '.audio', '.baby', '.band', '.bar', '.bargains', '.be', '.beer', '.berlin',
            '.best', '.bet', '.bid', '.bike', '.bingo', '.bio', '.biz', '.black', '.blackfriday',
            '.blog', '.blue', '.boston', '.boutique', '.br.com', '.build', '.builders', '.business',
            '.buzz', '.buz', '.ca', '.cab', '.cafe', '.camera', '.camp', '.capital', '.cards', '.care',
            '.careers', '.casa', '.cash', '.casino', '.catering', '.cc', '.center', '.ceo', '.ch', '.charity',
            '.chat', '.cheap', '.christmas', '.church', '.city', '.claims', '.cleaning', '.click', '.clinic',
            '.clothing', '.cloud', '.club', '.cn.com', '.co', '.co.com', '.co.in', '.co.nz', '.co.uk', '.coach',
            '.codes', '.coffee', '.college', '.com', '.com.co', '.com.mx', '.com.tw', '.community', '.company',
            '.computer', '.condos', '.construction', '.consulting', '.contact', '.contractors', '.cooking',
            '.cool', '.coupons', '.courses', '.credit', '.creditcard', '.cricket', '.cruises', '.cymru',
            '.cz', '.dance', '.date', '.dating', '.de', '.de.com', '.deals', '.degree', '.delivery',
            '.democrat', '.dental', '.dentist', '.desi', '.design', '.diamonds', '.diet', '.digital',
            '.direct', '.directory', '.discount', '.doctor', '.dog', '.domains', '.download', '.earth',
            '.eco', '.education', '.email', '.energy', '.engineer', '.engineering', '.enterprises',
            '.equipment', '.estate', '.eu', '.eu.com', '.events', '.exchange', '.expert', '.exposed',
            '.express', '.fail', '.faith', '.family', '.fans', '.farm', '.fashion', '.film', '.finance',
            '.financial', '.fish', '.fishing', '.fit', '.fitness', '.flights', '.florist', '.flowers', '.fm',
            '.football', '.forsale', '.foundation', '.fun', '.fund', '.furniture', '.futbol', '.fyi', '.gallery',
            '.games', '.garden', '.gay', '.gift', '.gifts', '.gives', '.glass', '.global', '.gmbh', '.gold',
            '.golf', '.graphics', '.gratis', '.green', '.gripe', '.group', '.gs', '.guide', '.guitars', '.guru',
            '.haus', '.healthcare', '.help', '.hiphop', '.hn', '.hockey', '.holdings', '.holiday', '.horse',
            '.host', '.hosting', '.house', '.how', '.immo', '.in', '.industries', '.info', '.ink', '.institue',
            '.insure', '.international', '.investments', '.io', '.irish', '.it', '.jetzt', '.jewelry', '.jp',
            '.jpn.com', '.juegos', '.kaufen', '.kim', '.kitchen', '.kiwi', '.la', '.land', '.lawyer', '.lease',
            '.legal', '.lgbt', '.li', '.life', '.lighting', '.limited', '.limo', '.link', '.live', '.llc', '.loan',
            '.loans', '.lol', '.london', '.love', '.ltd', '.luxury ', '.maison', '.managment', '.market', '.marketing',
            '.mba', '.me', '.me.uk', '.media', '.memorial', '.men', '.menu', '.miami', '.mobi', '.moda', '.moe', '.money',
            '.monster', '.mortgage', '.mx', '.nagoya', '.navy', '.net', '.net.co', '.network', '.news', '.ngo', '.ninja',
            '.nl', '.nyc', '.okinawa', '.one', '.ong', '.online', '.org', '.org.in', '.org.uk', '.partners', '.parts',
            '.party', '.pet', '.ph', '.photo', '.photography', '.photos', '.physio', '.pics', '.pictures', '.pink',
            '.pizza', '.pl', '.place', '.plumbing', '.plus', '.poker', '.press', '.pro', '.productions', '.promo',
            '.properties', '.property', '.pub', '.qpon', '.quebec', '.racing', '.realty', '.recipes', '.red', '.rehab',
            '.reisen', '.rent', '.rentals', '.repair', '.report', '.republican', '.rest', '.restaurant', '.review',
            '.reviews', '.rip', '.rocks', '.rodeo', '.run', '.sa.com', '.sale', '.sarl', '.sc', '.school', '.schule',
            '.science', '.se.net', '.services', '.sexy', '.sg', '.shiksha', '.shoes', '.shop', '.shopping', '.show',
            '.singles', '.site', '.ski', '.soccer', '.social', '.software', '.solar', '.solutions', '.soy', '.space',
            '.srl', '.store', '.stream', '.studio', '.study', '.style', '.supplies', '.supply', '.support', '.surf',
            '.surgery', '.systems', '.tattoo', '.tax', '.taxi', '.team', '.tech', '.technology', '.tel', '.tennis',
            '.theater', '.tienda', '.tips', '.today', '.tokyo', '.tools', '.tours', '.town', '.toys', '.trade', '.training',
            '.tv', '.tw', '.uk', '.uk.com', '.university', '.uno', '.us', '.us.com', '.vacations', '.vc', '.vegas',
            '.ventures', '.vet', '.viajes', '.video', '.villas', '.vip', '.vision', '.vodka', '.vote', '.voting',
            '.voyage', '.watch', '.webcam', '.website', '.wedding', '.wiki', '.win', '.wine', '.work', '.works',
            '.world', '.ws', '.wtf', '.xyz', '.yoga', '.za.com', '.zone']
POPULAR_EXTENTIONS = [
    '.com','.io','.ai','.net','.org','.co','.us'
    ]
ALL_EXTENTIONS = list(set(POPULAR_EXTENTIONS+EXTENTIONS))
ALL_URL_KEYS = {
    'scheme':['https','http'],
    'netloc':{
        "www":[True,False],
        "extentions":[POPULAR_EXTENTIONS,ALL_EXTENTIONS]
        }
    }

def domain_exists(host: str) -> bool:
    """Check if a domain resolves in DNS."""
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False

def get_extention(url=None, parsed=None, netloc=None, options=None):
    """
    Split netloc into {www, domain, extention}.
    Cycles through www + extension options until a working one is found.
    """
    options = options or ALL_URL_KEYS["netloc"]

    # Ensure we have a string netloc
    if url and not parsed:
        parsed = urlparse(url)
    if parsed and not netloc:
        netloc = parsed["netloc"] if isinstance(parsed, dict) else parsed.netloc
    if isinstance(netloc, dict):
        netloc = reconstructNetLoc(netloc)

    if not netloc:
        return {"www": False, "domain": "", "extention": ".com"}

    netloc = netloc.lower().strip()

    # detect existing www
    has_www = netloc.startswith("www.")
    if has_www:
        netloc = netloc[len("www.") :]

    # cycle through options
    www_opts = options["www"]
    ext_opts = options["extentions"][0] + options["extentions"][1]  # POPULAR + ALL

    # if the netloc already ends with a known extension, use it
    for ext in sorted(ALL_EXTENTIONS, key=len, reverse=True):
        if netloc.endswith(ext):
            domain = netloc[: -len(ext)]
            return {"www": has_www, "domain": domain, "extention": ext}

    # else, try combinations
    for www in www_opts:
        for ext in ext_opts:
            candidate = f"{'www.' if www else ''}{netloc}{ext}"
            if domain_exists(candidate):
                return {"www": www, "domain": netloc, "extention": ext}

    # fallback
    return {"www": has_www, "domain": netloc, "extention": ".com"}



def reconstructNetLoc(netloc):
    keys = ['www','domain','extention']
    if isinstance(netloc, dict):
        vals = []
        for key in keys:
            value = netloc.get(key)
            if key == 'www':
                value = 'www' if value else ''
            vals.append(eatAll(value or '', ['.']))
        netloc = eatAll('.'.join(vals), ['.'])
    return netloc or ''

def reconstructQuery(query):
    if isinstance(query, dict):
        # Keep stable ordering if you want: sort by key
        return "&".join(f"{k}={v}" for k, v in query.items())
    return query or ''

def reconstructUrlParse(url=None, parsed=None, parsed_dict=None):
    d = parse_url(url=url, parsed=parsed, parsed_dict=parsed_dict)
    return urlunparse((
        d.get("scheme") or "",
        reconstructNetLoc(d.get("netloc")),
        d.get("path") or "",
        d.get("params") or "",
        reconstructQuery(d.get("query")),
        d.get("fragment") or "",
    ))
def dictquery(parsed):
    query = parsed.query if hasattr(parsed, "query") else parsed
    if not query:
        return {}
    nuqueries = {}
    for pair in str(query).split("&"):
        if not pair:
            continue
        if "=" in pair:
            k, v = pair.split("=", 1)
            nuqueries[k] = v
        else:
            nuqueries[pair] = ""
    return nuqueries

def parse_netloc(url=None,parsed=None,netloc=None):
    netloc = get_extention(url=url,parsed=parsed,netloc=netloc)
    www=False
    nunetloc={'www':www}
    nunetloc.update(netloc)
    domain = nunetloc.get("domain")
    if domain.startswith('www.'):
        nunetloc['domain']=domain[len('www.'):]
        www = True
    nunetloc['www'] = www
    return nunetloc
from urllib.parse import urlparse, ParseResult, urlunparse

def parse_url(url=None, parsed=None, parsed_dict=None):
    """
    Accepts:
      - url: str
      - parsed: urllib.parse.ParseResult OR str (url) OR dict (already parsed)
      - parsed_dict: dict (already parsed)
    Returns a normalized dict with keys: scheme, netloc, path, params, query, fragment
    """
    # If caller already has a parsed dict, prefer that
    if isinstance(parsed_dict, dict):
        return parsed_dict

    # If caller accidentally passed dict into `parsed`, treat it as parsed_dict
    if isinstance(parsed, dict):
        return parsed

    # If `parsed` is actually a URL string, normalize to url
    if isinstance(parsed, str) and not url:
        url = parsed
        parsed = None

    # Build ParseResult if we have a URL and no parsed object
    if url and not isinstance(parsed, ParseResult):
        parsed = urlparse(url)

    # If we now have a real ParseResult, normalize it
    if isinstance(parsed, ParseResult):
        scheme = parsed.scheme or ALL_URL_KEYS["scheme"][0]

        # Handle bare "example" case (no scheme/netloc but a path with a hostname)
        netloc = parsed.netloc
        path   = parsed.path
        if not scheme and not netloc and path:
            parts = [p for p in path.split("/") if p]
            if parts:
                netloc = parts[0]
                path   = f"/{'/'.join(parts[1:])}" if len(parts) > 1 else ""
                # do not need to rebuild ParseResult; we only return dict

        netloc_data = get_extention(parsed=parsed, options=ALL_URL_KEYS["netloc"])
def reconstructUrlFromUrlParse(url=None, parsed=None, parsed_dict=None):
    keys = ['scheme','netloc','path','params','query','fragment']
    if url and not parsed:
        parsed_dict = parse_url(url=url)
    if parsed and not parsed_dict:
        parsed_dict = parse_url(parsed=parsed)
    if parsed_dict:
        scheme = parsed_dict.get('scheme')
        nuUrl = ''
        for key in keys:
            value = parsed_dict.get(key, '')
            if key == 'scheme':
                nuUrl += f'{value}://' if value else ''
            elif key == 'query':
                nuUrl += f'?{reconstructQuery(value)}' if value else ''
            elif key == 'netloc':
                nuUrl += reconstructNetLoc(value) if value else ''
            else:
                # removed noisy print(value)
                nuUrl += value
        return nuUrl
    return url

def get_youtube_url(url=None, parsed=None, parsed_dict=None):
    if url and not parsed:
        parsed_dict = parse_url(url=url)
    if parsed and not parsed_dict:
        parsed_dict = parse_url(parsed=parsed)
    if parsed_dict:
        netloc = parsed_dict.get("netloc")
        domain = (netloc or {}).get('domain') or ''
        query  = parsed_dict.get('query') or {}
        path   = parsed_dict.get('path') or ''
        if domain.startswith('youtu'):
            # force youtube.com and /watch?v=ID
            netloc['www'] = True
            netloc['domain'] = 'youtube'
            netloc['extention'] = '.com'
            parsed_dict['netloc'] = netloc

            # keep v if present; otherwise derive
            v_query = query.get('v')
            if not v_query:
                if path.startswith('/watch/') or path.startswith('/shorts/'):
                    v_query = eatAll(path, ['/','watch','shorts'])
                else:
                    v_query = eatAll(path, ['/'])
            parsed_dict['path'] = '/watch'
            parsed_dict['query'] = {'v': v_query} if v_query else {}
            return reconstructUrlFromUrlParse(parsed_dict=parsed_dict)
def get_threads_url(url=None,parsed=None, parsed_dict =None ):
    if url and not parsed:
        parsed = parse_url(url)
    if parsed and not parsed_dict:
        parsed_dict = parse_url(parsed=parsed)
    if parsed_dict:
        netloc = parsed_dict.get("netloc")
        domain = netloc.get('domain')
        if domain.startswith('threads'):
            netloc['www']=True
            netloc['domain'] ='youtube'
            netloc['extention'] = '.net'
            parsed['netloc']=netloc
            return reconstructUrlFromUrlParse(url=url,parsed=parsed,parsed_dict=None)  
def get_corrected_url(url=None,parsed=None, parsed_dict =None ):
    if url and not parsed:
        parsed_dict = parse_url(url=url)
    if parsed and not parsed_dict:
        parsed_dict = parse_url(parsed=parsed)
    if parsed_dict:
        funcs = [get_threads_url,get_youtube_url,reconstructUrlFromUrlParse]
        for func in funcs:
            corrected_url = func(url=url,parsed=parsed,parsed_dict=parsed_dict)
            if corrected_url:
                return corrected_url
        return {
            "scheme": scheme,
            "netloc": netloc_data,
            "path": path or "",
            "params": parsed.params or "",
            "query": dictquery(parsed),
            "fragment": parsed.fragment or "",
        }

    # Fallback: if we only have a URL string
    if isinstance(url, str):
        p = urlparse(url)
        return {
            "scheme": p.scheme or ALL_URL_KEYS["scheme"][0],
            "netloc": get_extention(parsed=p, options=ALL_URL_KEYS["netloc"]),
            "path": p.path or "",
            "params": p.params or "",
            "query": dictquery(p),
            "fragment": p.fragment or "",
        }

    # Last resort
    return {
        "scheme": ALL_URL_KEYS["scheme"][0],
        "netloc": {},
        "path": "",
        "params": "",
        "query": {},
        "fragment": "",
    }

