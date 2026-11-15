const PAGES = [
  { id: 'overview', label: 'Overview' },
  { id: 'observations', label: 'Observations' },
  { id: 'evidence', label: 'Evidence and Methods' },
]

function Sidebar({ currentPage, onNavigate }) {
  return (
    <aside className="sidebar">
      <div className="brand">
        <span className="brand-icon">🛰️</span>
        <span className="brand-name">Wayanad EarthWatch</span>
      </div>

      <nav className="nav">
        {PAGES.map((page) => (
          <button
            key={page.id}
            className={page.id === currentPage ? 'nav-item active' : 'nav-item'}
            onClick={() => onNavigate(page.id)}
          >
            {page.label}
          </button>
        ))}
      </nav>

      <p className="sidebar-note">
        Prototype. No real satellite data loaded yet.
      </p>
    </aside>
  )
}

export default Sidebar