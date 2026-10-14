import { useEffect, useMemo, useState } from 'react'
import { Activity, ArrowDown, ArrowLeft, ArrowRight, AudioLines, Check, ChevronDown, Disc3, Headphones, Heart, Library, ListMusic, LoaderCircle, Music2, Pause, Play, Plus, RefreshCw, Search, Settings2, Sparkles, ThumbsDown, Volume2, X } from 'lucide-react'

const API = import.meta.env.VITE_API_URL || ''
const moods = ['All moods', 'Easy listening', 'Feel good', 'Focused', 'Late night']
const palettes = [['#e6a0a1','#923f62'],['#dfc48b','#8f5b3b'],['#a3b1a4','#455a52'],['#c6a7d7','#674788'],['#e4a565','#a94c34'],['#9aa9d4','#44518b']]

async function request(path, options) {
  const response = await fetch(`${API}${path}`, { headers: { 'Content-Type': 'application/json', ...(options?.headers || {}) }, ...options })
  const body = await response.json().catch(() => ({}))
  if (!response.ok && response.status !== 202) throw new Error(body.detail || body.error || 'Something went wrong. Please try again.')
  return { status: response.status, body }
}
const splitList = value => value.split(',').map(item => item.trim()).filter(Boolean)
const trackName = track => track.track_name || track.name || 'Untitled track'
const artistName = track => track.artist || track.artists?.map(a => a.name).join(', ') || 'Unknown artist'

function App() {
  const [profile, setProfile] = useState(() => { try { return JSON.parse(localStorage.getItem('soundscape-profile')) } catch { return null } })
  const [tracks, setTracks] = useState([])
  const [analytics, setAnalytics] = useState(null)
  const [busy, setBusy] = useState(false)
  const [notice, setNotice] = useState('')
  const [query, setQuery] = useState('')
  const [mood, setMood] = useState('All moods')
  const [playing, setPlaying] = useState(null)
  const [showProfile, setShowProfile] = useState(false)
  const [mobileNav, setMobileNav] = useState(false)

  const load = async (id = profile?.id) => {
    if (!id) return
    setBusy(true)
    try {
      const [recommendation, stats] = await Promise.all([
        request(`/recommendations/${id}/`),
        request(`/analytics/user/${id}/`).catch(() => ({ body: null })),
      ])
      if (recommendation.body.recommendations) setTracks(recommendation.body.recommendations)
      else if (recommendation.body.message) setNotice('Your mix is being made. Use Refresh mix to check again in a moment.')
      setAnalytics(stats.body)
    } catch (error) { setNotice(error.message) }
    finally { setBusy(false) }
  }

  useEffect(() => { if (profile?.id) load(profile.id) }, [])
  const filtered = useMemo(() => tracks.filter(track => `${trackName(track)} ${artistName(track)}`.toLowerCase().includes(query.toLowerCase())), [tracks, query])

  const saveProfile = async data => {
    setBusy(true); setNotice('')
    try {
      const { body } = await request('/users/', { method: 'POST', body: JSON.stringify(data) })
      localStorage.setItem('soundscape-profile', JSON.stringify(body)); setProfile(body); setShowProfile(false); setNotice(`Welcome in, ${body.name.split(' ')[0]}. Your discovery mix is on its way.`)
      load(body.id)
    } catch (error) { setNotice(error.message) } finally { setBusy(false) }
  }

  const logAction = async (track, action) => {
    if (!profile?.id) return setShowProfile(true)
    try {
      await request('/analytics/activity/', { method: 'POST', body: JSON.stringify({ user: profile.id, track_name: trackName(track), artist: artistName(track), action }) })
      if (action === 'like') setNotice('Added to your liked tracks.')
      if (action === 'skip') setNotice('Got it. We’ll tune your mix.')
    } catch (error) { setNotice(error.message) }
  }

  const refresh = async () => {
    if (!profile) return setShowProfile(true)
    setBusy(true); setNotice('Your new mix is being put together.')
    try { await request(`/recommendations/${profile.id}/refresh/`, { method: 'POST' }); setNotice('Your mix is being made. Use Refresh mix to check again in a moment.') }
    catch (error) { setNotice(error.message) } finally { setBusy(false) }
  }

  return <div className="app-shell">
    <aside className={`sidebar ${mobileNav ? 'sidebar-open' : ''}`}>
      <a className="brand" href="#home"><span className="brand-icon"><AudioLines size={21}/></span><span>soundscape<span className="brand-dot">.</span></span></a>
      <div className="side-label">YOUR SPACE</div>
      <nav className="nav-list">
        <a className="nav-item active" href="#home" onClick={() => setMobileNav(false)}><Sparkles size={18}/> Discover</a>
        <a className="nav-item" href="#your-mix" onClick={() => setMobileNav(false)}><Library size={18}/> Your mix</a>
        <a className="nav-item" href="#recent" onClick={() => setMobileNav(false)}><Activity size={18}/> Listening stats</a>
      </nav>
      <div className="side-divider"/>
      <div className="side-label">YOUR LIBRARY</div>
      <button className="nav-item nav-button" onClick={() => setShowProfile(true)}><Plus size={18}/> Set up your profile</button>
      <div className="sidebar-spacer"/>
      <div className="sidebar-note"><div className="note-orbit"><Headphones size={22}/></div><p>Good music finds you when you least expect it.</p><span>KEEP YOUR EARS OPEN</span></div>
      <button className="profile-mini" onClick={() => setShowProfile(true)}><span className="avatar">{profile?.name?.[0]?.toUpperCase() || '♪'}</span><span className="profile-copy"><b>{profile?.name || 'Make it personal'}</b><small>{profile?.email || 'Set up your profile'}</small></span><Settings2 size={17}/></button>
    </aside>
    {mobileNav && <button className="mobile-scrim" onClick={() => setMobileNav(false)} aria-label="Close menu"/>}
    <main className="main-content" id="home">
      <header className="topbar"><button className="mobile-menu icon-button" onClick={() => setMobileNav(!mobileNav)} aria-label="Open menu"><ListMusic size={20}/></button><div className="crumb">Your personal listening room <span>/</span> <b>Discover</b></div><div className="top-actions"><button className="spotify-button" onClick={() => { window.location.href = `${API}/spotify/login/` }}><span className="spotify-mark">●</span> Connect Spotify <ArrowRight size={15}/></button><button className="avatar top-avatar" onClick={() => setShowProfile(true)}>{profile?.name?.[0]?.toUpperCase() || '♪'}</button></div></header>
      <div className="content-wrap">
        <section className="hero">
          <div className="hero-copy"><div className="eyebrow"><span className="live-dot"/> A LITTLE SOMETHING FOR YOUR EARS</div><h1>Find your<br/><em>next favorite.</em></h1><p>A fresh listening experience, shaped around you.<br className="desktop-break"/> No digging required.</p><div className="hero-actions"><a href="#your-mix" className="primary-button">Explore your mix <ArrowDown size={16}/></a><button className="text-button" onClick={() => setShowProfile(true)}>{profile ? 'Edit your profile' : 'Make it yours'} <ArrowRight size={15}/></button></div></div>
          <div className="hero-art" aria-hidden="true"><div className="art-glow"/><div className="art-ring ring-one"/><div className="art-ring ring-two"/><div className="art-vinyl"><div className="vinyl-lines"/><div className="vinyl-label"><span>SS</span></div></div><div className="floating-note note-one">♪</div><div className="floating-note note-two">♫</div><div className="art-caption"><span>NOW SPINNING</span><b>something new</b></div></div>
          <div className="hero-index"><span>01</span><div/><span>03</span></div>
        </section>
        {notice && <div className="notice"><span>{notice}</span><button onClick={() => setNotice('')} aria-label="Dismiss"><X size={15}/></button></div>}
        <section className="section-heading" id="your-mix"><div><div className="eyebrow muted">MADE FOR YOUR MOMENT</div><h2>Your discovery mix<span className="green-dot">.</span></h2><p>A few picks we think you’ll love today.</p></div><button className="refresh-button" onClick={refresh} disabled={busy}><RefreshCw size={16} className={busy ? 'spinning' : ''}/> Refresh mix</button></section>
        <div className="filter-row"><div className="search-box"><Search size={17}/><input aria-label="Search tracks" placeholder="Find a track or artist..." value={query} onChange={e => setQuery(e.target.value)}/>{query && <button onClick={() => setQuery('')} aria-label="Clear search"><X size={14}/></button>}</div><div className="mood-select"><Sparkles size={16}/><select value={mood} onChange={e => setMood(e.target.value)} aria-label="Filter by mood">{moods.map(item => <option key={item}>{item}</option>)}</select><ChevronDown size={14}/></div><span className="results-count">{filtered.length ? `${filtered.length} TRACKS` : 'YOUR NEXT LISTEN'}</span></div>
        <div className="track-grid">{filtered.length ? filtered.slice(0, 6).map((track, index) => <TrackCard key={track.id || `${trackName(track)}-${index}`} track={track} index={index} playing={playing === index} onPlay={() => { setPlaying(playing === index ? null : index); logAction(track, 'play') }} onLike={() => logAction(track, 'like')} onSkip={() => logAction(track, 'skip')}/>) : tracks.length ? <div className="empty-state">No tracks match that search. Try another title or artist.</div> : <div className="empty-state"><span className="empty-icon"><Disc3 size={24}/></span><b>{busy ? 'Finding your sound…' : 'Your mix is ready when you are'}</b><p>{profile ? 'We’re pulling together some music for you.' : 'Create a quick profile and we’ll start learning your taste.'}</p><button className="primary-button" onClick={() => profile ? load() : setShowProfile(true)}>{busy ? <LoaderCircle size={16} className="spinning"/> : profile ? 'Try again' : 'Build my profile'} <ArrowRight size={15}/></button></div>}</div>
        <section className="bottom-row" id="recent"><div className="listening-card"><div className="listening-title"><div><div className="eyebrow muted">THE LITTLE THINGS ADD UP</div><h3>Your listening lately</h3></div><span className="stat-icon"><Activity size={18}/></span></div><div className="stats"><div><b>{analytics?.plays ?? '—'}</b><span>LISTENS</span><div className="stat-line"><i style={{width: analytics?.plays ? '73%' : '8%'}}/></div></div><div><b>{analytics?.likes ?? '—'}</b><span>LIKED</span><div className="stat-line"><i style={{width: analytics?.likes ? '48%' : '8%'}}/></div></div><div><b>{analytics?.skips ?? '—'}</b><span>SKIPPED</span><div className="stat-line"><i style={{width: analytics?.skips ? '28%' : '8%'}}/></div></div></div></div><div className="quote-card"><span className="quote-mark">“</span><p>Music is the shorthand of emotion.</p><div><span/><small>LEO TOLSTOY</small></div><div className="quote-spark">✳</div></div></section>
        <footer><span>MADE FOR THE WAY YOU LISTEN.</span><span>TAKE THE LONG WAY HOME <Music2 size={13}/></span></footer>
      </div>
    </main>
    {showProfile && <ProfileModal profile={profile} onClose={() => setShowProfile(false)} onSave={saveProfile} busy={busy}/>}
  </div>
}

function TrackCard({ track, index, playing, onPlay, onLike, onSkip }) {
  const [a, b] = palettes[index % palettes.length]
  return <article className="track-card"><div className="cover" style={{'--cover-a': a, '--cover-b': b}}><div className="cover-orb"/><div className="cover-lines"/><span className="cover-mark">{index % 2 ? 'SOUND<br/>IN COLOR' : 'SIDE<br/>A'}</span><button className="play-button" onClick={onPlay} aria-label={playing ? 'Pause' : 'Play'}>{playing ? <Pause size={18} fill="currentColor"/> : <Play size={18} fill="currentColor"/>}</button><span className="cover-number">0{index + 1}</span></div><div className="track-info"><div className="track-meta"><span className="track-tag">{track.album?.name || 'A fresh find'}</span><button className="more-button" onClick={onSkip} title="Not for me"><ThumbsDown size={15}/></button></div><h3 title={trackName(track)}>{trackName(track)}</h3><p>{artistName(track)}</p><div className="track-footer"><span><AudioLines size={14}/> {track.duration_ms ? `${Math.floor(track.duration_ms / 60000)}:${String(Math.floor(track.duration_ms / 1000) % 60).padStart(2, '0')}` : 'DISCOVERY'}</span><button className="like-button" onClick={onLike} title="Like track"><Heart size={17}/></button></div></div></article>
}

function ProfileModal({ profile, onClose, onSave, busy }) {
  const [name, setName] = useState(profile?.name || '')
  const [email, setEmail] = useState(profile?.email || '')
  const [genres, setGenres] = useState((profile?.favorite_genres || []).join(', '))
  const [artists, setArtists] = useState((profile?.favorite_artists || []).join(', '))
  const [moodsValue, setMoodsValue] = useState((profile?.moods || []).join(', '))
  const submit = event => { event.preventDefault(); onSave({ name, email, favorite_genres: splitList(genres), favorite_artists: splitList(artists), moods: splitList(moodsValue) }) }
  return <div className="modal-backdrop" onMouseDown={event => { if (event.target === event.currentTarget) onClose() }}><form className="profile-modal" onSubmit={submit}><div className="modal-top"><span className="modal-icon"><Sparkles size={19}/></span><button type="button" className="icon-button" onClick={onClose} aria-label="Close"><X size={19}/></button></div><div className="eyebrow muted">LET’S GET TO KNOW YOU</div><h2>Your taste, your space.</h2><p className="modal-intro">A few details help us find the right sound for your day.</p><label>Your name<input required value={name} onChange={e => setName(e.target.value)} placeholder="What should we call you?"/></label><label>Email address<input type="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="you@example.com"/></label><label>Favorite genres <span>SEPARATE WITH COMMAS</span><input value={genres} onChange={e => setGenres(e.target.value)} placeholder="indie, jazz, electronic"/></label><label>Artists you love <span>OPTIONAL</span><input value={artists} onChange={e => setArtists(e.target.value)} placeholder="The xx, Khruangbin…"/></label><label>Moods you gravitate to <span>OPTIONAL</span><input value={moodsValue} onChange={e => setMoodsValue(e.target.value)} placeholder="calm, upbeat, focused"/></label><button className="primary-button modal-submit" disabled={busy}>{busy ? <LoaderCircle size={16} className="spinning"/> : <Check size={16}/>} {profile ? 'Save my profile' : 'Create my profile'} <ArrowRight size={15}/></button><small className="privacy-note">Your preferences stay yours. We use them to shape your recommendations.</small></form></div>
}

export default App
