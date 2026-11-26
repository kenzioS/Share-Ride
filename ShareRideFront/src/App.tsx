import './App.css'

function App() {
  return (
    <div className="page">
      <header className="site-header">
        <a className="brand" href="/">
          ShareRide
        </a>
        <nav className="nav" aria-label="Main navigation">
          <button type="button" className="nav-button">
            Profile
          </button>
          <button type="button" className="nav-button">
            Rides
          </button>
          <button type="button" className="nav-button">
            Reviews
          </button>
        </nav>
      </header>

      <main className="main-content">
        <section className="welcome">
          <div className="welcome-text">
            <h1>Welcome to ShareRide</h1>
            <p className="lead">
              ShareRide makes everyday travel simpler by connecting drivers with
              empty seats to passengers heading the same way.
            </p>
            <p>
              Post a ride you are offering or find one that fits your route, then
              arrange the details together. Share the road, split the costs, and
              travel with people going your direction.
            </p>
          </div>
        </section>
      </main>
    </div>
  )
}

export default App
