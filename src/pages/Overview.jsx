import Card from '../components/Card'

function Overview() {
  return (
    <div>
      <h1>Overview</h1>
      <p>Evidence-first landslide monitoring with NISAR satellite data.</p>

      <Card title="Study area">
        <p>Wayanad district, Kerala, India.</p>
      </Card>

      <Card title="Current evidence status">
        <p>
          No NISAR observations have been loaded or verified yet. Nothing on
          this site should be read as a landslide detection or a warning.
        </p>
      </Card>

      <Card title="Planned data sources (not yet used)">
        <p>
          NISAR products from NASA Earthdata and the ASF DAAC. Other sources,
          such as rainfall, terrain, geology and land cover, will be added
          only after we verify their coverage, dates and licenses.
        </p>
      </Card>

      <Card title="What this platform cannot do">
        <p>
          It cannot predict sudden landslides. Satellite observations may help
          show certain surface changes, but they do not give guaranteed
          advance warning.
        </p>
      </Card>
    </div>
  )
}

export default Overview