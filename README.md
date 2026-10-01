# Curriculum Portfolio Analytics

[![Validate analysis](https://github.com/hand-lauraelizabeth/curriculum-portfolio-analytics/actions/workflows/validate.yml/badge.svg)](https://github.com/hand-lauraelizabeth/curriculum-portfolio-analytics/actions/workflows/validate.yml)

A synthetic portfolio-management example showing how curriculum and learning-product data can be structured for decision support.

This repository models a training portfolio across formats, topics, delivery modes, lifecycle stages, and utilization signals. All data are synthetic and created for demonstration only.

## Results at a glance

| Metric | Synthetic result |
| --- | ---: |
| Learning products | 18 |
| Topics | 8 |
| Formats | 5 |
| Registrations | 2,180 |
| Attendees | 1,252 |
| Portfolio attendance rate | 57.4% |
| Average completion rate | 86.9% |
| Average satisfaction | 4.45 / 5 |

### Registrations by topic

| Topic | Registrations |
| --- | ---: |
| AI & Technology | 559 |
| Data & Measurement | 372 |
| Customer Experience | 312 |
| Creative | 291 |
| Brand Strategy | 198 |
| Communications | 163 |
| Leadership | 157 |
| Marketing Operations | 128 |

### Highest demonstration utilization scores

| Product | Score |
| --- | ---: |
| Prompting for Strategic Work | 85.0 |
| Customer Journey Blueprint | 82.3 |
| Creative Briefs That Work | 80.2 |
| Applied AI Foundations | 76.0 |
| Dashboard Storytelling | 74.4 |

### Refresh candidates

| Product | Stage | Score | Months since refresh |
| --- | --- | ---: | ---: |
| Content Strategy Systems | Refresh | 52.2 | 30.1 |
| Agency Relationship Management | Refresh | 55.1 | 25.8 |
| Experiment Design for Marketers | Refresh | 57.7 | 28.5 |

The utilization score and refresh rules are demonstration logic applied to synthetic data, not a real organization's performance thresholds.

## What this demonstrates

- Curriculum portfolio modeling
- Learning-product taxonomy design
- Utilization and demand analysis
- Format and topic segmentation
- Portfolio QA and lifecycle management
- Decision-support metrics for curriculum planning
- Privacy-conscious reconstruction of professional methods

## Example questions

The project is designed to answer questions such as:

- Which topics have the strongest utilization?
- Which formats are under- or over-represented?
- Where are there portfolio gaps?
- Which learning products may need refresh, consolidation, or expansion?
- How can topic demand and delivery footprint inform development priorities?

## Repository structure

```
curriculum-portfolio-analytics/
├── .github/workflows/
│   └── validate.yml
├── analysis/
│   └── portfolio_summary.py
├── data/
│   └── synthetic_curriculum_portfolio.csv
├── docs/
│   └── data_dictionary.md
├── README.md
└── requirements.txt
```

## Quick start

```bash
pip install -r requirements.txt
python analysis/portfolio_summary.py
```

## Privacy note

No employer, faculty, client, member, learner, revenue, or proprietary program data are included. The schema, thresholds, titles, and examples are generalized and synthetic.

---

**Laura Elizabeth Hand**  
[Portfolio](https://www.lauraelizabethhand.com/) · [LinkedIn](https://www.linkedin.com/in/lauraelizabethhand)
