import Card from '../components/Card'
import EvidenceBadge from '../components/EvidenceBadge'

const LABEL_GUIDE = [
  { type: 'observed', text: 'What a dataset directly shows.' },
  { type: 'derived', text: 'A value we calculated from observed data.' },
  { type: 'possible', text: 'A reasonable reading, not a conclusion.' },
  { type: 'validation', text: 'Needs independent checking.' },
  { type: 'none', text: 'The data does not support it.' },
]

function EvidenceMethods() {
  return (
    <div>
      <h1>Evidence and Methods</h1>

      <Card title="How we label evidence">
        {LABEL_GUIDE.map((item) => (
          <p key={item.type}>
            <EvidenceBadge type={item.type} /> {item.text}
          </p>
        ))}
      </Card>
    </div>
  )
}

export default EvidenceMethods