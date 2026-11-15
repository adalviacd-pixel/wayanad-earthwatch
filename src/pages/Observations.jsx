import { useEffect, useState } from 'react'
import Card from '../components/Card'
import EvidenceBadge from '../components/EvidenceBadge'

function Observations() {
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch('/data/pairs.json')
      .then((res) => {
        if (!res.ok) throw new Error('Could not load pairs.json')
        return res.json()
      })
      .then(setData)
      .catch((err) => setError(err.message))
  }, [])

  if (error) return <p>{error}</p>
  if (!data) return <p>Loading observations...</p>

  return (
    <div>
      <h1>Observations</h1>

      <Card title={data.dataset}>
        <p>
          <EvidenceBadge type="observed" /> Product maturity: {data.maturity}
        </p>
        <p>Window: {data.window}.</p>
        <p>{data.caution}</p>
      </Card>

      <Card title="Interferometric pairs (12-day repeat unless noted)">
        <div className="table-wrap">
          <table className="data-table">
            <thead>
              <tr>
                <th>First date</th>
                <th>Second date</th>
                <th>Gap (days)</th>
                <th>Mean coherence</th>
                <th>Phase spread (rad)</th>
                <th>Iono flag (%)</th>
              </tr>
            </thead>
            <tbody>
              {data.pairs.map((p) => (
                <tr key={p.product}>
                  <td>{p.start}</td>
                  <td>{p.end}</td>
                  <td>{p.gap_days}</td>
                  <td>{p.coherence_mean.toFixed(2)}</td>
                  <td>{p.phase_std_rad.toFixed(2)}</td>
                  <td>{p.iono_flag_pct.toFixed(1)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p>
          <EvidenceBadge type="observed" /> dates, gap.{' '}
          <EvidenceBadge type="derived" /> coherence, phase spread, flag share
          (computed from valid pixels in the window).{' '}
          <EvidenceBadge type="none" /> No displacement or landslide
          interpretation.
        </p>
      </Card>
    </div>
  )
}

export default Observations