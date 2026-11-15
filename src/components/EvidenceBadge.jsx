const LABELS = {
  observed: 'Observed',
  derived: 'Derived',
  possible: 'Possible interpretation',
  validation: 'Requires validation',
  none: 'Not established',
}

function EvidenceBadge({ type }) {
  return <span className={`badge badge-${type}`}>{LABELS[type]}</span>
}

export default EvidenceBadge