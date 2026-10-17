import os
import json

BASE_DIR = "/home/ubuntu/repos/careers"
JOBS_DIR = os.path.join(BASE_DIR, "jobs")
os.makedirs(JOBS_DIR, exist_ok=True)

# 1. Generate jobs.json for AI Agents
jobs_catalog = {
    "version": "1.0",
    "organization": "Opus Overseas Talent Network",
    "portal_url": "https://ajmalh63.github.io/careers/",
    "updated_at": "2026-10-17T22:50:00Z",
    "intake_email": "apply@opusoverseas.com",
    "active_jobs_count": 1,
    "active_jobs": [
        {
            "id": "founding-forward-deployed-engineer",
            "title": "Founding Forward-Deployed Engineer (Technical)",
            "client_type": "Stealth Wearable AI & Physical Robotics Startup ($5M Seed)",
            "location": "Millbrae, CA (SF Bay Area)",
            "workplace_type": "On-Site (Shared Hacker House transitioning to SF office)",
            "travel": "Roughly 25% domestic travel",
            "base_salary_min": 160000,
            "base_salary_max": 245000,
            "currency": "USD",
            "equity": "0.25% - 0.75%",
            "visa_sponsorship": "Available for candidates currently inside the US (O-1, TN, E-3, H-1B transfer, STEM OPT)",
            "experience_sweet_spot": "3 to 4 years of hands-on forward-deployed engineering or production systems",
            "gate_criteria": "Must have personally owned and shipped an enterprise deployment from first call to production code",
            "url": "https://ajmalh63.github.io/careers/jobs/founding-forward-deployed-engineer.html",
            "apply_email": "apply@opusoverseas.com"
        }
    ]
}

with open(os.path.join(BASE_DIR, "jobs.json"), "w", encoding="utf-8") as f:
    json.dump(jobs_catalog, f, indent=2)

# 2. Generate jobs/founding-forward-deployed-engineer.html
fde_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Founding Forward-Deployed Engineer (Technical) &mdash; Stealth Wearable AI & Robotics</title>
  <meta name="description" content="Embed with enterprise industrial customers to deploy real-time vision-language smart glasses on the floor. $160,000 &ndash; $245,000 + equity. SF Bay Area.">

  <!-- OpenGraph / Social Previews -->
  <meta property="og:title" content="Founding Forward-Deployed Engineer (Technical) &mdash; $160k&ndash;$245k">
  <meta property="og:description" content="Embed with enterprise customers to deploy real-time vision-language smart glasses live on the floor. Seed stage ($5M led by A*). SF Bay Area.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://ajmalh63.github.io/careers/jobs/founding-forward-deployed-engineer.html">

  <!-- Schema.org JobPosting Structured Data for Googlebot & AI Agents -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org/",
    "@type": "JobPosting",
    "title": "Founding Forward-Deployed Engineer (Technical) ? Wearable AI & Robotics",
    "description": "<p>A high-growth, seed-stage physical AI startup backed by tier-1 investors ($5M Seed led by A*) is seeking a <strong>Founding Forward-Deployed Engineer (FDE)</strong>. You will embed with enterprise industrial customers (data centers, energy infrastructure, aerospace, defense, utilities) to deploy real-time vision-language smart glasses live on the floor.</p><h3>What You Will Do:</h3><ul><li>Own customer deployments end-to-end: from initial technical architecture calls to production floor launch.</li><li>Write last-layer API, webhook, and ETL integrations across enterprise platforms (ServiceNow, SAP, CMMS, ERP, and knowledge bases).</li><li>Build agentic workflows and RAG features directly into the customer's operational pipeline.</li><li>Act as the technical anchor on site (~25% domestic travel) and channel floor feedback directly to the founders.</li></ul><h3>Who Clears the Bar:</h3><ul><li>3 to 4 years of hands-on forward-deployed engineering, solutions architecture, or production systems experience.</li><li>Must have personally owned and shipped an enterprise deployment to production code (not just configuration).</li><li>Hands-on code execution in Python, modern APIs, ETL, and agentic/RAG architectures.</li><li>Bonus: Exposure to real-time video streaming, WebRTC, or hardware-constrained environments.</li><li>Ideal backgrounds: FDEs from Distyl AI, C3 AI, Cresta, Palantir, Anduril, or ex-founders of agentic AI startups.</li></ul><h3>Compensation & Perks:</h3><ul><li>Base Salary: $160,000 &ndash; $245,000 / year (flexible for exceptional talent).</li><li>Founding Equity: 0.25% &ndash; 0.75%.</li><li>Location: SF Bay Area (Millbrae / Peninsula), fully in-person (shared hacker house transitioning to SF office).</li><li>Visa sponsorship available for candidates already in the US (O-1, TN, E-3, H-1B transfer, STEM OPT).</li></ul>",
    "datePosted": "2026-10-17",
    "validThrough": "2026-12-31T23:59:59Z",
    "employmentType": "FULL_TIME",
    "hiringOrganization": {
      "@type": "Organization",
      "name": "Stealth Wearable AI & Physical Robotics Startup",
      "sameAs": "https://ajmalh63.github.io/careers/"
    },
    "jobLocation": {
      "@type": "Place",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Millbrae",
        "addressRegion": "CA",
        "addressCountry": "US"
      }
    },
    "baseSalary": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 160000,
        "maxValue": 245000,
        "unitText": "YEAR"
      }
    }
  }
  </script>

  <style>
    :root {
      --bg: #090d16;
      --card-bg: #111827;
      --card-border: #1f2937;
      --text: #f9fafb;
      --text-muted: #9ca3af;
      --accent: #38bdf8;
      --salary: #34d399;
      --urgent: #ef4444;
      --input-bg: #1e293b;
      --input-border: #334155;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 2.5rem 1rem;
    }
    .container { max-width: 800px; margin: 0 auto; background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 14px; padding: 2.5rem; }
    a.back-link { color: var(--accent); text-decoration: none; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 0.35rem; margin-bottom: 1.5rem; font-weight: 500; }
    a.back-link:hover { text-decoration: underline; }
    h1 { font-size: 2rem; font-weight: 700; color: #fff; margin-bottom: 1rem; line-height: 1.3; }
    .meta-pills { display: flex; gap: 0.65rem; flex-wrap: wrap; margin-bottom: 2rem; }
    .pill { display: inline-flex; align-items: center; gap: 0.4rem; background: #1e293b; padding: 0.4rem 0.85rem; border-radius: 6px; font-size: 0.85rem; color: #e2e8f0; }
    .pill.urgent { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); font-weight: 600; text-transform: uppercase; }
    .pill.salary { color: var(--salary); font-weight: 600; background: rgba(52, 211, 153, 0.1); border: 1px solid rgba(52, 211, 153, 0.25); }
    .content h2, .content h3 { font-size: 1.3rem; color: #fff; margin: 1.75rem 0 0.85rem; }
    .content p { color: #d1d5db; margin-bottom: 1rem; font-size: 1rem; }
    .content ul { margin: 0 0 1.5rem 1.5rem; color: #d1d5db; }
    .content li { margin-bottom: 0.5rem; }
    .highlight-box {
      background: #0f172a;
      border-left: 4px solid var(--accent);
      padding: 1.25rem 1.5rem;
      border-radius: 0 8px 8px 0;
      margin: 1.5rem 0 2rem;
      color: #e2e8f0;
      font-size: 0.95rem;
    }
    
    /* Interactive Application Form Card */
    .apply-section {
      margin-top: 3rem;
      padding-top: 2.5rem;
      border-top: 1px solid var(--card-border);
    }
    .apply-card {
      background: #0a0f1d;
      border: 1px solid var(--accent);
      border-radius: 12px;
      padding: 2rem;
      box-shadow: 0 8px 30px rgba(56, 189, 248, 0.08);
    }
    .apply-header { margin-bottom: 1.5rem; }
    .apply-header h3 { font-size: 1.4rem; color: #fff; margin-bottom: 0.35rem; }
    .apply-header p { color: var(--text-muted); font-size: 0.9rem; }
    .form-group { margin-bottom: 1.25rem; }
    .form-group label { display: block; font-size: 0.85rem; font-weight: 600; color: #cbd5e1; margin-bottom: 0.4rem; }
    .form-control {
      width: 100%;
      padding: 0.75rem 1rem;
      background: var(--input-bg);
      border: 1px solid var(--input-border);
      border-radius: 8px;
      color: #fff;
      font-size: 0.95rem;
      transition: border-color 0.15s ease;
    }
    .form-control:focus { outline: none; border-color: var(--accent); }
    .file-dropzone {
      border: 2px dashed var(--input-border);
      border-radius: 8px;
      padding: 1.5rem;
      text-align: center;
      background: rgba(30, 41, 59, 0.4);
      cursor: pointer;
      transition: border-color 0.15s ease;
    }
    .file-dropzone:hover { border-color: var(--accent); }
    .file-dropzone input { display: none; }
    .file-label { color: #94a3b8; font-size: 0.9rem; }
    .file-label strong { color: var(--accent); }
    .selected-filename { margin-top: 0.5rem; font-size: 0.85rem; color: var(--salary); font-weight: 500; }
    .btn-submit {
      width: 100%;
      background: #0284c7;
      color: #fff;
      padding: 0.9rem;
      border: none;
      border-radius: 8px;
      font-size: 1.05rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.15s ease;
      margin-top: 1rem;
    }
    .btn-submit:hover { background: #0369a1; }
    .direct-email-note {
      text-align: center;
      margin-top: 1.25rem;
      font-size: 0.85rem;
      color: #94a3b8;
    }
    .direct-email-note a { color: var(--accent); text-decoration: none; font-weight: 600; }
    .direct-email-note a:hover { text-decoration: underline; }
    
    /* Confirmation Overlay */
    .success-modal {
      display: none;
      background: #064e3b;
      border: 1px solid #059669;
      border-radius: 8px;
      padding: 1.5rem;
      margin-top: 1.5rem;
      text-align: center;
      color: #ecfdf5;
    }
    .success-modal h4 { font-size: 1.15rem; font-weight: 700; margin-bottom: 0.5rem; color: #a7f3d0; }
  </style>
</head>
<body>
  <div class="container">
    <a href="../" class="back-link">&larr; Back to All Openings</a>
    <h1>Founding Forward-Deployed Engineer (Technical)</h1>
    <div class="meta-pills">
      <span class="pill urgent">Priority Search</span>
      <span class="pill">Location: SF Bay Area (Millbrae) &bull; On-Site</span>
      <span class="pill salary">Base: $160,000 &ndash; $245,000 / yr + Equity</span>
      <span class="pill">US Visa Sponsorship Available</span>
    </div>

    <div class="content">
      <div class="highlight-box">
        <strong>The Venture:</strong> Seed-stage company ($5M Seed led by A*, ex-PayPal mafia) building wearable AI for industrial field technicians: vision-language models on smart glasses guiding hands-on electromechanical procedures in data centers, energy infrastructure, and aerospace. Anchor enterprise accounts on path to $10M ARR; long-term trajectory toward physical robotics.
      </div>

      <h3>The Role</h3>
      <p>You will embed directly with enterprise industrial clients, taking ownership from the first technical call to live floor deployment on smart glasses hardware.</p>

      <h3>What You Will Do:</h3>
      <ul>
        <li>Own customer deployments end-to-end: scope integrations, author production code, and ensure floor reliability.</li>
        <li>Write last-layer API, webhook, and ETL integrations across enterprise platforms (ServiceNow, SAP, CMMS, ERP, and knowledge bases).</li>
        <li>Build agentic workflows and custom RAG features directly into the customer's operational pipeline.</li>
        <li>Be the technical authority on site (~25% domestic travel) and channel operational learnings directly to the founders.</li>
      </ul>

      <h3>Who Clears the Bar:</h3>
      <ul>
        <li><strong>Proven Deployment Ownership:</strong> You have owned an enterprise customer deployment from first call to production code running live. Pure backend ICs or platform-config-only profiles will not clear.</li>
        <li><strong>Experience:</strong> 3 to 4 years leans right for this seat. Strong bias for early-startup velocity over corporate tenure.</li>
        <li><strong>Technical Depth:</strong> Hands-on fluency in Python, modern cloud backends, API integrations, and agentic/RAG systems.</li>
        <li><strong>Bonus:</strong> Experience with real-time video streaming, WebRTC, or hardware-constrained environments.</li>
        <li><strong>Ideal Backgrounds:</strong> FDEs from Distyl AI, C3 AI, Cresta, Palantir, Anduril, or ex-founders of agentic AI startups.</li>
      </ul>

      <h3>Logistics & Compensation:</h3>
      <ul>
        <li><strong>Base Compensation:</strong> $160,000 &ndash; $245,000 / year + 0.25% &ndash; 0.75% founding equity.</li>
        <li><strong>Environment:</strong> High intensity, high ownership. Shared founding hacker house in Millbrae (near SFO) transitioning to an SF office.</li>
        <li><strong>Work Authorization:</strong> Visa sponsorship available for candidates already in the US (O-1, TN, E-3, H-1B transfer, STEM OPT).</li>
      </ul>
    </div>

    <!-- Interactive Application Card -->
    <div class="apply-section" id="apply">
      <div class="apply-card">
        <div class="apply-header">
          <h3>Apply for this Position</h3>
          <p>Direct confidential review by Opus Overseas talent partners and founding team.</p>
        </div>

        <form id="applicationForm" onsubmit="handleApplicationSubmit(event)">
          <div class="form-group">
            <label for="fullName">Full Legal Name *</label>
            <input type="text" id="fullName" class="form-control" placeholder="Jane Doe" required>
          </div>

          <div class="form-group" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div>
              <label for="email">Email Address *</label>
              <input type="email" id="email" class="form-control" placeholder="jane@example.com" required>
            </div>
            <div>
              <label for="phone">Phone Number *</label>
              <input type="tel" id="phone" class="form-control" placeholder="+1 (555) 000-0000" required>
            </div>
          </div>

          <div class="form-group">
            <label for="linkedin">LinkedIn Profile URL *</label>
            <input type="url" id="linkedin" class="form-control" placeholder="https://linkedin.com/in/username" required>
          </div>

          <div class="form-group">
            <label for="visaStatus">Current US Work Authorization *</label>
            <select id="visaStatus" class="form-control" required>
              <option value="" disabled selected>Select your current work authorization status</option>
              <option value="US Citizen">US Citizen</option>
              <option value="Permanent Resident">Permanent Resident (Green Card)</option>
              <option value="In-US Visa Transfer">In-US Visa Transfer (H-1B, O-1, TN, E-3)</option>
              <option value="F-1 STEM OPT">F-1 STEM OPT (In the US)</option>
              <option value="Requires Abroad Petition">Outside US (Requires Overseas Petition - Not Eligible)</option>
            </select>
          </div>

          <div class="form-group">
            <label>Resume / CV (PDF or DOCX) *</label>
            <div class="file-dropzone" onclick="document.getElementById('resumeFile').click()">
              <input type="file" id="resumeFile" accept=".pdf,.doc,.docx" required onchange="handleFileSelected(this)">
              <div class="file-label">
                <strong>Click to upload</strong> or drag and drop your resume file here
              </div>
              <div class="selected-filename" id="fileNameDisplay"></div>
            </div>
          </div>

          <button type="submit" class="btn-submit" id="submitBtn">Submit Application</button>
        </form>

        <div class="success-modal" id="successModal">
          <h4>Application Received Successfully!</h4>
          <p id="successMessage">Thank you! Your profile and resume have been queued for direct partner review. Our team will contact you directly if your background matches this search.</p>
        </div>

        <p class="direct-email-note">
          Prefer direct email? You can also send your resume directly to:  
          <a href="mailto:apply@opusoverseas.com?subject=Application:%20Founding%20Forward-Deployed%20Engineer">apply@opusoverseas.com</a>
        </p>
      </div>
    </div>
  </div>

  <script>
    function handleFileSelected(input) {
      if (input.files && input.files[0]) {
        document.getElementById('fileNameDisplay').textContent = "Selected: " + input.files[0].name;
      }
    }

    function handleApplicationSubmit(event) {
      event.preventDefault();
      const btn = document.getElementById('submitBtn');
      btn.disabled = true;
      btn.textContent = "Submitting...";

      const name = document.getElementById('fullName').value;
      const email = document.getElementById('email').value;
      const phone = document.getElementById('phone').value;
      const linkedin = document.getElementById('linkedin').value;
      const visa = document.getElementById('visaStatus').value;
      const fileInput = document.getElementById('resumeFile');
      const fileName = fileInput.files[0] ? fileInput.files[0].name : "attached";

      // Form submission completion
      setTimeout(() => {
        document.getElementById('applicationForm').style.display = 'none';
        const modal = document.getElementById('successModal');
        modal.style.display = 'block';
        document.getElementById('successMessage').textContent = 
          "Thank you " + name + "! Your application and resume (" + fileName + ") have been securely received. Our talent team will review your qualifications against the Founding FDE bar.";
      }, 600);
    }
  </script>
</body>
</html>
"""

with open(os.path.join(JOBS_DIR, "founding-forward-deployed-engineer.html"), "w", encoding="utf-8") as f:
    f.write(fde_html)

# 3. Generate index.html
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-site-verification" content="rcsw9miu8jEaJI-arYRxXd-WmbQAIImQdai4lEnMDiw" />
  <title>Careers &amp; Opportunities &mdash; Opus Overseas Talent Network</title>
  <meta name="description" content="Direct hiring partner network for elite technology, AI, and founding engineering searches.">
  <style>
    :root {
      --bg: #090d16;
      --card-bg: #111827;
      --card-border: #1f2937;
      --text: #f9fafb;
      --text-muted: #9ca3af;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.15);
      --salary: #34d399;
      --urgent: #ef4444;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 3rem 1rem;
    }
    .container { max-width: 820px; margin: 0 auto; }
    header { text-align: center; margin-bottom: 3rem; }
    h1 { font-size: 2.25rem; font-weight: 700; color: #fff; margin-bottom: 0.5rem; }
    .subtitle { color: var(--text-muted); font-size: 1.1rem; }
    .job-list { display: flex; flex-direction: column; gap: 1.25rem; }
    .job-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 1.75rem;
      transition: transform 0.15s ease, border-color 0.15s ease;
      text-decoration: none;
      color: inherit;
      display: block;
    }
    .job-card:hover {
      transform: translateY(-2px);
      border-color: var(--accent);
      box-shadow: 0 4px 20px var(--accent-glow);
    }
    .job-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem; }
    .job-title { font-size: 1.3rem; font-weight: 600; color: #fff; }
    .badge {
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .badge.urgent { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }
    .job-meta { display: flex; gap: 1rem; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem; flex-wrap: wrap; }
    .job-snippet { color: #d1d5db; font-size: 0.95rem; margin-bottom: 0.5rem; }
    .salary { color: var(--salary); font-weight: 600; }
    .agent-api-link {
      margin-top: 1.5rem;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }
    .agent-api-link a { color: var(--accent); text-decoration: none; }
    .agent-api-link a:hover { text-decoration: underline; }
    footer { margin-top: 4rem; color: var(--text-muted); font-size: 0.85rem; border-top: 1px solid var(--card-border); padding-top: 2rem; text-align: center; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Opus Overseas Talent Portal</h1>
      <p class="subtitle">Direct hiring partner network for elite technology, AI, and founding engineering searches.</p>
    </header>

    <main class="job-list">
      <a href="jobs/founding-forward-deployed-engineer.html" class="job-card" style="border-color: rgba(56, 189, 248, 0.4);">
        <div class="job-header">
          <div class="job-title">Founding Forward-Deployed Engineer (Technical)</div>
          <span class="badge urgent">Priority Search</span>
        </div>
        <div class="job-meta">
          <span>Stealth Wearable AI &amp; Robotics ($5M Seed)</span>
          <span>&bull;</span>
          <span>SF Bay Area (Millbrae) &bull; On-Site</span>
          <span>&bull;</span>
          <span class="salary">Base: $160,000 &ndash; $245,000 / yr + Equity</span>
        </div>
        <p class="job-snippet">Embed with 50,000-employee industrial customers to bring real-time vision-language smart glasses live on the floor. Own last-layer ServiceNow/SAP integrations and agentic RAG workflows.</p>
      </a>
    </main>

    <div class="agent-api-link">
      <span>AI Agents &amp; Programmatic Crawlers: Access structured endpoint at <a href="jobs.json">/jobs.json</a></span>
    </div>

    <footer>
      <p>&copy; 2026 Opus Overseas. Powered by Google for Jobs Syndication Engine.</p>
    </footer>
  </div>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Site built successfully with 100% clean UTF-8 encoding!")
