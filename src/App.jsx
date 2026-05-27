import './App.css'

function App() {
  const metrics = [
    { label: 'Compliance Score', value: '92%', trend: '+4.8% this month' },
    { label: 'Open Findings', value: '14', trend: '3 high-priority' },
    { label: 'Automation Coverage', value: '78%', trend: '+12 workflows added' },
    { label: 'Assurance Readiness', value: '87%', trend: 'On track for Q3 audit' },
  ]

  const modules = [
    {
      title: 'Emissions Intelligence',
      description:
        'Track scope 1, 2, and 3 emissions with anomaly detection and source-level drilldowns.',
      status: 'Live',
    },
    {
      title: 'Policy & Control Center',
      description:
        'Map regulatory controls to internal policies, evidence, and owner accountability.',
      status: 'In review',
    },
    {
      title: 'Supplier Risk Monitor',
      description:
        'Continuously monitor supplier ESG posture with alerts for violations and expiring attestations.',
      status: 'Live',
    },
    {
      title: 'AI Gap Analyzer',
      description:
        'Prioritize material risks and generate remediation plans with estimated impact scores.',
      status: 'Updated 2h ago',
    },
  ]

  const portfolioCompanies = [
    { name: 'Siemens AG', sector: 'Industrial', score: 87, risk: 'Low' },
    { name: 'Volkswagen AG', sector: 'Automotive', score: 72, risk: 'Medium' },
    { name: 'BASF SE', sector: 'Chemicals', score: 79, risk: 'Medium' },
    { name: 'SAP SE', sector: 'Technology', score: 91, risk: 'Low' },
    { name: 'Bayer AG', sector: 'Healthcare', score: 68, risk: 'High' },
  ]

  return (
    <div className="page">
      <header className="topbar">
        <div className="brand">
          <span className="brand-mark">ESG</span>
          <p>ESG Intelligence</p>
        </div>
        <button type="button" className="primary-button">
          Request Demo
        </button>
      </header>

      <section className="hero-section">
        <div>
          <p className="eyebrow">Governance. Sustainability. Assurance.</p>
          <h1>Stay ahead of ESG regulations with a single intelligent platform.</h1>
          <p className="hero-copy">
            Bring policy controls, emissions reporting, supplier compliance, and board-level
            disclosures into one auditable workflow.
          </p>
          <div className="hero-actions">
            <button type="button" className="primary-button">
              Start Assessment
            </button>
            <button type="button" className="secondary-button">
              View Compliance Map
            </button>
          </div>
        </div>

        <div className="hero-panel">
          <p className="panel-title">Framework Coverage</p>
          <div className="pill-row">
            <span>CSRD</span>
            <span>GRI</span>
            <span>ISSB</span>
            <span>TCFD</span>
          </div>
          <div className="progress-block">
            <div>
              <p>Mandatory Disclosure Completion</p>
              <strong>84%</strong>
            </div>
            <div className="progress-track">
              <div className="progress-value" />
            </div>
          </div>
        </div>
      </section>

      <section className="metric-grid">
        {metrics.map((item) => (
          <article key={item.label} className="metric-card">
            <p>{item.label}</p>
            <h2>{item.value}</h2>
            <small>{item.trend}</small>
          </article>
        ))}
      </section>

      <section className="content-grid">
        <div className="module-list">
          <div className="section-head">
            <h3>Compliance Modules</h3>
            <button type="button" className="ghost-button">
              Manage
            </button>
          </div>
          <div className="module-grid">
            {modules.map((module) => (
              <article key={module.title} className="module-card">
                <div className="module-top">
                  <h4>{module.title}</h4>
                  <span>{module.status}</span>
                </div>
                <p>{module.description}</p>
              </article>
            ))}
          </div>

          <div className="company-portfolio">
            <h4>Company Portfolio</h4>
            <p>Real-time ESG monitoring across 5 companies</p>
            <div className="company-table">
              <div className="row head">
                <span>Company</span>
                <span>Sector</span>
                <span>ESG Score</span>
                <span>Risk Level</span>
              </div>
              {portfolioCompanies.map((company) => (
                <div key={company.name} className="row">
                  <span>{company.name}</span>
                  <span>{company.sector}</span>
                  <span>{company.score}</span>
                  <span>{company.risk}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        <aside className="report-card">
          <h3>Board Reporting Snapshot</h3>
          <p>
            Ready-to-publish disclosure drafts with confidence levels and linked source evidence.
          </p>
          <ul>
            <li>
              <span>Climate Risk Narrative</span>
              <strong>Ready</strong>
            </li>
            <li>
              <span>Gender Pay Equity</span>
              <strong>Pending</strong>
            </li>
            <li>
              <span>Human Rights Review</span>
              <strong>Ready</strong>
            </li>
            <li>
              <span>Waste Circularity Index</span>
              <strong>Needs Data</strong>
            </li>
          </ul>
          <button type="button" className="primary-button full">
            Export ESG Report
          </button>
        </aside>
      </section>
    </div>
  )
}

export default App
