# VisionSpark — Project Rules for Claude

## TOOLS POLICY — FREE ONLY

**Always use free tools exclusively.** This is a hard rule, not a preference.

- Never recommend or use a paid tool without explicitly flagging it first
- When a paid tool would be relevant, always provide a free alternative in the same response
- Format: "⚠️ [Tool] is paid. Free alternative: [X]"

### Free Tool Stack (approved)
| Purpose | Free Tool |
|---------|-----------|
| Design / Pinterest pins | Canva (free tier) — `pinterest_pin` design type |
| AI image model in Canva | Ideogram v3 (free via Canva), Canva default AI |
| Presentations / decks | Gamma (free tier) |
| Documentation / planning | Notion (free tier) |
| Code & version control | Git + GitHub |
| Deploy / hosting | Netlify (free tier) |
| Product sales | Gumroad (free tier) |
| Web search & research | WebSearch + WebFetch (built-in) |
| Python image gen (fallback only) | Pillow — open source, free |

### Paid Tools — Do Not Use Without Flagging
- Figma Editor seat (View-only is free — editing requires paid plan)
- Canva Pro features (Pro badge on any template/element)
- Any MCP tool that requires a paid subscription not already active

## PROJECT OVERVIEW

**Brand:** VisionSpark (`visionsparkinnovation.com`)
**Platform:** Netlify (live deploy)
**Shop:** Gumroad (`psyinsight.gumroad.com`)

### Products
| # | Name | Price | Gumroad |
|---|------|-------|---------|
| 01 | From Zero to First Sale | $13 | psyinsight.gumroad.com/l/qscjsb |
| 02 | The Personal Reset System™ | $17 | psyinsight.gumroad.com/l/uxhty |

### Content System
- Each product gets a **3-post blog arc** + **3 Pinterest pins**
- Arc 1 (Product 01): `how-i-made-my-first-1000-online.html`, `48-hour-digital-product.html`, `why-price-your-first-product-at-13.html`
- Arc 2 (Product 02): `why-i-blew-up-my-routine.html`, `5-module-reset-rebuild-habits-30-days.html`, `habit-myth-discipline-is-not-a-strategy.html`
- Blog lives in `/blog/`, homepage in `/homepage/`
- Pinterest pins: 1000×1500px, 2:3 ratio, editorial design system

### Design System
| Token | Value |
|-------|-------|
| Oat (bg) | #FAF6ED |
| Ink (text) | #2A2218 |
| Forest (accent 1) | #3B6E5A |
| Amber (accent 2) | #C9892A |
| Terracotta (accent 3) | #A8513A |
| Sand (border) | #D4C9B8 |
| Taupe (secondary) | #8A7E70 |
| Gold (nav) | #f4a900 |

### Branch
All work on: `claude/beautiful-hypatia-cAPHh`
