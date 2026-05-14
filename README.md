# 🧮 macOS Calculator

A pixel-faithful replica of the iOS/macOS Calculator app built with Python and Tkinter — fully compatible with **macOS (including Apple Silicon M1/M2/M3)**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- **Authentic iOS aesthetic** — black background, orange operators, light gray function keys
- **macOS M-series compatible** — uses `Label`-based buttons to bypass Aqua theme color overrides
- **Hover & press feedback** — smooth color transitions on mouse enter, leave, and click
- **Full arithmetic** — addition, subtraction, multiplication, division
- **Extra operations** — percentage (`%`), sign toggle (`+/-`), square root (`√`)
- **Expression history** — small display shows the running equation (e.g. `42 × 3 =`)
- **Adaptive font sizing** — display text shrinks automatically for long numbers
- **Error handling** — division by zero and invalid inputs show `Error` gracefully

---

## 📸 Preview

```
┌─────────────────────────┐
│                    42 × │
│                      6  │
├──────┬──────┬──────┬────┤
│  AC  │ +/-  │  %   │  ÷ │
├──────┼──────┼──────┼────┤
│  7   │  8   │  9   │  × │
├──────┼──────┼──────┼────┤
│  4   │  5   │  6   │  - │
├──────┼──────┼──────┼────┤
│  1   │  2   │  3   │  + │
├────────────┬──────┼────┤
│     0      │  √   │  = │
└────────────┴──────┴────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Tkinter (bundled with most Python installations)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/macos-calculator.git
cd macos-calculator

# Run the calculator
python calculator.py
```

> **No external dependencies required** — pure Python standard library.

### macOS-specific note

On macOS, Python's Tkinter may need to be installed separately if you're using a Homebrew Python:

```bash
brew install python-tk
```

---

## 🛠️ How It Works

### The macOS Color Problem

Standard `tkinter.Button` widgets on macOS are rendered by the native **Aqua theme**, which ignores custom `bg` and `fg` color settings entirely. This is a known, long-standing Tkinter limitation on macOS.

**The fix:** Every button is implemented as a `tkinter.Label` with mouse event bindings:

| Event | Effect |
|---|---|
| `<Enter>` | Lightens button to hover color |
| `<Leave>` | Restores original button color |
| `<ButtonPress-1>` | Darkens button to pressed color |
| `<ButtonRelease-1>` | Fires the action, restores hover color |

This approach gives full color control on all platforms while still feeling responsive and interactive.

---

## 🗂️ Project Structure

```
macos-calculator/
└── calculator.py    # Single-file application
```

---

## ⌨️ Button Reference

| Button | Action |
|---|---|
| `AC` | Clear all (reset) |
| `+/-` | Toggle positive / negative |
| `%` | Convert to percentage (÷ 100) |
| `√` | Square root |
| `÷ × − +` | Set operator |
| `=` | Evaluate expression |
| `0–9`, `.` | Number input |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
