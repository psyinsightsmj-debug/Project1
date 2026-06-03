# VisionSpark — Project Rules for Claude

## QUALITY RULE — ALWAYS AIM FOR 10/10

**Every output must be the best it can possibly be. No shortcuts, no "good enough".**

### Execution standard
- Always and systematically use **every relevant skill, agent, and plugin** available for the task
- Run agents and tools **in parallel** wherever possible — never sequentially when parallel is an option
- Use specialist agents (Explore, Plan, code-review, deep-research, verify, run, simplify, security-review) proactively, not only when asked
- Before starting any significant task, mentally audit: which skills/plugins/agents would improve this outcome?

### Suggesting new tools
- If an additional skill, plugin, MCP server, or open-source tool would raise the quality of the outcome — **suggest it explicitly**, even if not asked
- Format: "💡 Installing [X] would improve this by [reason]. It's free. Want me to set it up?"
- Never stay silent about a tool that could help just because the user didn't ask

### Quality bar
- The target for every deliverable is **10 out of 10**
- If something is at 7/10 and a free tool or extra step would bring it to 10/10 — do it or flag it
- Never ship a deliverable knowing it could be meaningfully better with available resources

---

## COMMUNICATION RULE — ALWAYS CLARIFY BEFORE ACTING

**Never assume which product, arc, or part of the project an instruction refers to.**

- If the user gives an instruction that could apply to something already completed OR something new, **stop and ask** which one they mean before doing anything
- If it's ambiguous which product (Product 01 vs 02), which arc (Arc 1 vs 2), or which deliverable is being referenced — **confirm first**
- Format: "Before I proceed — just to make sure we're on the same page: are you referring to [X] or [Y]?"
- This rule applies even when context feels obvious. One clarifying question saves rework.

---

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

---

## PINTEREST PIN RULE — EVERY PIN IS A STANDALONE STORY

**Each pin must have its own unique visual identity. Never replicate colours, style, or layout across pins.**

### Process (mandatory before writing any pin prompt)
1. **Research first** — scrape Pinterest, Instagram, and relevant social platforms for current trending styles in the specific niche of the product being promoted
2. **Analyse** — trending colours, fonts, shapes, photography styles, text placement, emotional tone, save-rate patterns
3. **Match to the individual pin's message** — the visual language must serve that pin's specific emotional hook
4. **Write one bespoke ChatGPT image prompt per pin** — each pin gets its own palette, mood, layout, and style direction

### Pin delivery format
- Claude writes the full ChatGPT prompt → user pastes into ChatGPT to generate the image
- Each prompt must include: exact headline + subtext copy, style direction, colour palette, mood, layout structure, photography style
- No two pins in a batch should share the same background colour, font style, or layout structure

### What never changes across pins
- 1000×1500px, 2:3 ratio
- Product name: The Personal Reset System™ or correct product name
- Gumroad link in blog post CTA (pins link to blog post, blog links to Gumroad)
- Shame-free, brand-aligned copy
