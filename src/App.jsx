import { useState } from 'react'
import Sidebar from './components/Sidebar'
import Overview from './pages/Overview'
import Observations from './pages/Observations'
import EvidenceMethods from './pages/EvidenceMethods'
import './App.css'

function App() {
  const [currentPage, setCurrentPage] = useState('overview')

  return (
    <div className="app-layout">
      <Sidebar currentPage={currentPage} onNavigate={setCurrentPage} />
      <main className="main-content">
        {currentPage === 'overview' && <Overview />}
        {currentPage === 'observations' && <Observations />}
        {currentPage === 'evidence' && <EvidenceMethods />}
      </main>
    </div>
  )
}

export default App