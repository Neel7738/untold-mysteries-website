<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vedic Science Explorer</title>
    <style>
        /* Modern styling with an Indian theme */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f3e6;
            color: #333;
            line-height: 1.6;
        }
        header {
            background: linear-gradient(135deg, #ff9933, #138808);
            color: white;
            text-align: center;
            padding: 2rem 0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .intro {
            text-align: center;
            margin-bottom: 3rem;
        }
        .animation-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
            display: flex;
            flex-direction: column;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card img {
            width: 100%;
            border-radius: 5px;
            height: 200px;
            object-fit: cover;
        }
        .card h3 {
            color: #138808;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }
        .card p {
            flex-grow: 1;
            margin-bottom: 1.5rem;
        }
        .youtube-button {
            background-color: #FF0000;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s;
            align-self: flex-start;
            margin-top: auto;
        }
        .youtube-button:hover {
            background-color: #CC0000;
        }
        .youtube-button::before {
            content: "▶ ";
        }
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 3rem;
        }
        @media (max-width: 768px) {
            .animation-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Vedic Science Explorer</h1>
        <p>Discover India's Ancient Scientific Legacy</p>
    </header>

    <div class="container">
        <section class="intro">
            <h2>Explore India's Contributions to Science</h2>
            <p>Interactive animations and resources for schools, based on ancient Indian texts.</p>
        </section>

        <section class="animation-grid">
            <div class="card">
                <img src="https://media.geeksforgeeks.org/wp-content/uploads/20220929133116/Whoinventedzero.png" alt="Zero Concept">
                <h3>The Concept of Zero (Śūnya)</h3>
                <p>How Indian mathematicians like Brahmagupta pioneered the use of zero as a number.</p>
                <button class="youtube-button" onclick="window.open('https://www.youtube.com/watch?v=uQBmSSe9_nw', '_blank')">
                    Watch Video
                </button>
            </div>
            <div class="card">
                <img src="https://thaka.bing.com/th/id/OIP.thCcOO47OMC1jJQYh-1zfgHaDb?w=336&h=161&c=7&r=0&o=5&dpr=1.3&pid=1.7" alt="Baudhayana Theorem">
                <h3>Baudhayana's Geometry</h3>
                <p>The Pythagorean theorem in the Sulba Sutras (800 BCE).</p>
                <button class="youtube-button" onclick="window.open('https://youtu.be/JaHnlp0PtgI', '_blank')">
                    Watch Video
                </button>
            </div>
            <div class="card">
                <img src="https://images.yourstory.com/cs/2/96eabe90392211eb93f18319e8c07a74/Image5hx4-1693673024248.jpg?fm=png&auto=format" alt="Sushruta Surgery">
                <h3>Sushruta's Surgical Tools</h3>
                <p>Ancient surgical techniques described in the Sushruta Samhita.</p>
                <button class="youtube-button" onclick="window.open('https://youtu.be/AIuKuYZ-bd8', '_blank')">
                    Watch Video
                </button>
            </div>
            <div class="card">
                <img src="https://www.thefamouspeople.com/profiles/images/aryabhata-5.jpg" alt="Aryabhata Astronomy">
                <h3>Aryabhata's Heliocentrism</h3>
                <p>How Aryabhata proposed Earth's rotation in the 5th century.</p>
                <button class="youtube-button" onclick="window.open('https://youtu.be/LI6mzQvNRRs', '_blank')">
                    Watch Video
                </button>
            </div>
            <div class="card">
                <img src="https://miro.medium.com/v2/resize:fit:1024/0*wEbUV2iA_5OkCoKq.jpg" alt="Panini Linguistics">
                <h3>Panini's Linguistics</h3>
                <p>The world's first formal grammar system (Ashtadhyayi).</p>
                <button class="youtube-button" onclick="window.open('https://youtu.be/9us3XTNkejE', '_blank')">
                    Watch Video
                </button>
            </div>
            <div class="card">
                <img src="https://www.ancient-origins.net/sites/default/files/field/image/Indian-sage-Acharya-Kanad.jpg" alt="Kanad Atomic Theory">
                <h3>Kanad's Atomic Theory</h3>
                <p>Vaisheshika school's ideas about atoms (2,600 years ago).</p>
                <button class="youtube-button" onclick="window.open('https://youtu.be/AaC-gMbNhMI', '_blank')">
                    Watch Video
                </button>
            </div>
        </section>
    </div>

    <footer>
        <p>© 2025 Vedic Science Explorer | Designed for Educational Use</p>
        <p>Contact: schools@vedicscienceexplorer.com</p>
    </footer>
</body>
</html>
