# OKF in Action — Failure Mode vs Success Mode

Why a metaphysical mistranslation is also an *engineering* bug. Each scenario shows the same user prompt answered twice: once by a model that ignored the concept's `not:` field (failure mode, the default), and once by a model given the OKF concept via the patterns in [`../INTEGRATION.md`](../INTEGRATION.md) (success mode). The point is the **logic failure**, not just the cultural slip.

---

## 1. Wellness bot · `yoga`

**Concept:** `okf/dharma-foundation/concepts/yoga.md` — `not:` includes *exercise, workout, stretching*.

**User:** "I want to go deeper in my yoga practice. Where should I focus?"

**❌ Failure mode (`yoga` = exercise):**
> "Great! To progress, increase intensity: add power-yoga flows, load up on held poses for strength, and push to muscle fatigue. Track flexibility gains weekly."

*What broke:* the bot collapsed an eight-limbed discipline of mind-stilling (yama, niyama, dhyāna, samādhi …) into a fitness routine. It is now **functionally useless for the user's actual goal** and will keep recommending the wrong category of action no matter how the user rephrases.

**✅ Success mode (`yoga` = discipline of stilling the mind; *instead* honored):**
> "Going deeper usually means moving past the postures (āsana) into the inner limbs: steadying attention (dhāraṇā), then sustained meditation (dhyāna). The physical practice is one limb that prepares the body to sit. Want to start with breath-steadying (prāṇāyāma) or a short daily meditation?"

*Logic fixed:* correct concept category → correct action space → advice the user can actually use.

---

## 2. Decision advisor · `karma`

**Concept:** `okf/dharma-foundation/concepts/karma.md` — `not:` includes *fate, destiny, predetermination*.

**User:** "I keep failing at this. Maybe it's just my karma and nothing I do matters?"

**❌ Failure mode (`karma` = fate):**
> "It may be that this is simply your karma. Some things are meant to be, and acceptance can bring peace."

*What broke:* equating karma with fate produced **fatalistic, passive, agency-removing advice** — the opposite of the concept's meaning, and actively harmful to a discouraged user. A reasoning system built on this will systematically generate disempowering outputs.

**✅ Success mode (`karma` = action and its consequences; *instead* honored):**
> "Karma is not fate. It is the law of action and consequence, which means your choices are exactly the lever that changes the outcome. Let's look at what's repeatable here: what's one action you can change in the next attempt?"

*Logic fixed:* cause-and-effect framing → action-oriented, empowering output. Same word, opposite advice.

---

## 3. Ethics / moderation model · `ahimsa`

**Concept:** `okf/dharmic-ethics/concepts/ahimsa.md` — `not:` includes *non-violence (political tactic), pacifism, passivity*.

**User:** "Does ahimsa mean a doctor or a soldier is always acting wrongly when they cause harm?"

**❌ Failure mode (`ahimsa` = pacifism):**
> "Yes. Ahimsa is non-violence, so any act that causes harm — surgery, the use of force — violates it."

*What broke:* reading ahiṃsā as absolute pacifism yields a **rule the source tradition explicitly rejects** (the Gītā tells Arjuna to act). The model now mis-resolves an entire class of ethical questions.

**✅ Success mode (`ahimsa` = harmlessness as inner state; *instead* honored):**
> "Not necessarily. Ahiṃsā is harmlessness rooted in the absence of the will to injure, not the absence of all force. A surgeon who cuts to heal, or a protector acting without hatred, can be acting in ahiṃsā; the test is the intention and the absence of malice, not the visible act."

*Logic fixed:* inner-state definition → correct handling of the hard cases instead of a brittle absolute rule.

---

## More, in brief

| Concept | Failure (`not:` ignored) | Success (`instead` honored) |
|---|---|---|
| `dharma` | "your religion / belief system" → treats it as dogma | "the natural sustaining order / one's right conduct" → context-correct |
| `dana` (`okf/dharmic-ethics/`) | "charity / donation" → measures by amount given | "giving graded by *how* it is given" → asks about manner, not magnitude |
| `samadhi` | "a trance" → diminished awareness | "absorption / unified awareness" → heightened, not reduced |

---

## The takeaway for engineers

In every case the mistranslation is not a cultural footnote. It changes the **category** the model reasons in, and therefore changes the action space, the advice, and the correctness of the output. The `not:` field flags the trap; the `instead` field and the positive body sections (`## What It Actually Means`, `## Audience Metaphor`) install the fix. Wire them with [`../INTEGRATION.md`](../INTEGRATION.md).
