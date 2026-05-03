import os
import glob

html_files = glob.glob('c:/Users/JEEVAN/Desktop/TESTING/IPA/templates/*.html')

css = """
    <!-- THEME INJECTION -->
    <style>
        [data-theme="dark"] {
            --bg-light: #111827;
            --bg-base: #111827;
            --bg: #111827;
            --surface: #1f2937;
            --card-bg: #1f2937;
            --text-main: #f9fafb;
            --text-primary: #f9fafb;
            --text-muted: #9ca3af;
            --text-secondary: #9ca3af;
            --border: #374151;
            --card-border: #374151;
            --icon-bg: #374151;
            --gradient-text: linear-gradient(135deg, #f9fafb 0%, #9ca3af 100%);
        }

        body, nav, .topbar, .session-info-bar, .question-card, .timer-card, .video-container, .badge, .status-badge, .guidance-panel, .guidance-text, span, h4, div, .subject-card, .difficulty-card, .feature-card, .stats-empty-state, .split-layout, .brand-panel, .form-card, section, header, main, h1, h2, h3, p {
            transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
        }

        .theme-toggle-btn {
            background: transparent;
            border: none;
            color: var(--text-muted, var(--text-secondary, #6b7280));
            cursor: pointer;
            padding: 0.5rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background-color 0.3s ease, color 0.3s ease;
            z-index: 9999;
        }

        .theme-toggle-btn:hover {
            background-color: var(--border, var(--card-border, #e5e7eb));
            color: var(--text-main, var(--text-primary, #111827));
        }

        .theme-toggle-btn svg {
            width: 24px;
            height: 24px;
        }

        .fixed-theme-toggle {
            position: fixed;
            top: 1rem;
            right: 1.5rem;
            background: var(--surface, var(--card-bg, #ffffff));
            border: 1px solid var(--border, var(--card-border, #e5e7eb));
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
    </style>
"""

btn_nav = """
        <!-- THEME TOGGLE -->
        <button id="themeToggle" class="theme-toggle-btn" aria-label="Toggle Theme">
            <svg id="sunIcon" style="display: none;" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
            <svg id="moonIcon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>
        </button>
"""

btn_fixed = """
    <!-- THEME TOGGLE FIXED -->
    <button id="themeToggle" class="theme-toggle-btn fixed-theme-toggle" aria-label="Toggle Theme">
        <svg id="sunIcon" style="display: none;" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
        <svg id="moonIcon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>
    </button>
"""

js = """
    <!-- THEME SCRIPT -->
    <script>
        const initTheme = () => {
            const savedTheme = localStorage.getItem('theme');
            const sunIcon = document.getElementById('sunIcon');
            const moonIcon = document.getElementById('moonIcon');
            if (savedTheme === 'dark') {
                document.documentElement.setAttribute('data-theme', 'dark');
                if (sunIcon) sunIcon.style.display = 'block';
                if (moonIcon) moonIcon.style.display = 'none';
            } else {
                document.documentElement.setAttribute('data-theme', 'light');
                if (sunIcon) sunIcon.style.display = 'none';
                if (moonIcon) moonIcon.style.display = 'block';
            }
        };

        const savedThemeInit = localStorage.getItem('theme');
        if (savedThemeInit === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
        }

        document.addEventListener("DOMContentLoaded", () => {
            initTheme();
            const themeToggleBtn = document.getElementById('themeToggle');
            const sunIcon = document.getElementById('sunIcon');
            const moonIcon = document.getElementById('moonIcon');

            if (themeToggleBtn) {
                themeToggleBtn.addEventListener('click', () => {
                    const currentTheme = document.documentElement.getAttribute('data-theme');
                    let targetTheme = 'light';
                    if (currentTheme === 'light' || !currentTheme) {
                        targetTheme = 'dark';
                        if (sunIcon) sunIcon.style.display = 'block';
                        if (moonIcon) moonIcon.style.display = 'none';
                    } else {
                        targetTheme = 'light';
                        if (sunIcon) sunIcon.style.display = 'none';
                        if (moonIcon) moonIcon.style.display = 'block';
                    }
                    document.documentElement.setAttribute('data-theme', targetTheme);
                    localStorage.setItem('theme', targetTheme);
                });
            }
        });
    </script>
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "THEME INJECTION" in content:
        print(f"Skipping {file_path}")
        continue

    # 1. Inject CSS before </head>
    content = content.replace("</head>", f"{css}\n</head>")

    # 2. Inject Button
    if '<div class="nav-actions">' in content:
        content = content.replace('<div class="nav-actions">', f'<div class="nav-actions">\n{btn_nav}')
    elif '<div class="topbar">' in content:
        # For index.html, we place it near the brand title
        content = content.replace('<div class="topbar">', f'<div class="topbar">\n{btn_nav}')
    else:
        # For subjects, difficulty, login, register, etc
        content = content.replace("<body>", f"<body>\n{btn_fixed}")

    # 3. Inject JS before </body>
    content = content.replace("</body>", f"{js}\n</body>")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {file_path}")
