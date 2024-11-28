// Camera database
const cameras = [
    { name: "Panasonic Lumix TZ200", price: 700, type: "Photography", features: ["Compact", "Travel zoom", "Versatile"] },
    { name: "Fujifilm GFX 100S", price: 6000, type: "Photography", features: ["Medium format", "High resolution", "Professional"] },
    { name: "Nikon Z fc", price: 1000, type: "Photography", features: ["APS-C", "Retro design", "Compact"] },
    { name: "Canon PowerShot SX740 HS", price: 400, type: "Photography", features: ["Compact", "Superzoom", "Entry-level"] },
    { name: "Panasonic Lumix FZ300", price: 600, type: "Photography", features: ["Bridge camera", "Superzoom", "Weather-sealed"] },
    { name: "Nikon Coolpix W300", price: 400, type: "Photography", features: ["Waterproof", "Compact", "Adventure-friendly"] },
    { name: "Fujifilm X100V", price: 1400, type: "Photography", features: ["Fixed lens", "Compact", "Retro style"] },
    { name: "Olympus Tough TG-6", price: 500, type: "Photography", features: ["Waterproof", "Adventure-friendly", "Compact"] },
    { name: "Canon EOS Rebel T7", price: 500, type: "Photography", features: ["DSLR", "Beginner-friendly", "APS-C"] },
    { name: "Pentax K-70", price: 700, type: "Photography", features: ["DSLR", "Weather-sealed", "APS-C"] },
    { name: "Panasonic Lumix GX85", price: 800, type: "Photography", features: ["Compact", "Micro Four Thirds", "Beginner-friendly"] },
    { name: "Fujifilm X-Pro3", price: 1800, type: "Photography", features: ["APS-C", "Retro style", "Professional"] },
    { name: "Leica M11", price: 9000, type: "Photography", features: ["Full-frame", "Luxury build", "Rangefinder"] },
    { name: "Ricoh GR IIIx", price: 1000, type: "Photography", features: ["Compact", "Fixed lens", "Street photography"] },
    { name: "Nikon D7500", price: 1000, type: "Photography", features: ["DSLR", "APS-C", "Intermediate"] },
    { name: "Sony Alpha a5000", price: 500, type: "Photography", features: ["Mirrorless", "Compact", "Beginner-friendly"] },
    { name: "Panasonic Lumix ZS100", price: 500, type: "Photography", features: ["Compact", "Travel zoom", "Beginner-friendly"] },
    { name: "Nikon Z9", price: 5500, type: "Hybrid", features: ["Full-frame", "Photography", "Videography"] },
    { name: "Fujifilm X-T30 II", price: 900, type: "Hybrid", features: ["APS-C", "Photography", "Videography"] },
    { name: "Sony Alpha a6000", price: 600, type: "Photography", features: ["APS-C", "Compact", "Beginner-friendly"] }
];

document.addEventListener("DOMContentLoaded", function() {
    // Get the current page
    const currentPage = window.location.pathname;

    // Input Page Logic
    if (currentPage.includes('index.html')) {
        const showResultsButton = document.getElementById('showResultsButton');
        const budgetInput = document.getElementById('budget');
        const functionalitySelect = document.getElementById('functionality');

        showResultsButton.addEventListener('click', function() {
            const budget = parseInt(budgetInput.value);
            const functionality = functionalitySelect.value;

            // Validate input
            if (!budget || budget <= 0) {
                alert("Please enter a valid budget.");
                return;
            }

            // Store data in localStorage
            localStorage.setItem('budget', budget);
            localStorage.setItem('functionality', functionality);

            // Navigate to results page
            window.location.href = 'results.html';
        });
    }

    // Results Page Logic
    if (currentPage.includes('results.html')) {
        const resultDiv = document.getElementById('result');
        const backButton = document.getElementById('backButton');

        // Retrieve stored data
        const budget = parseInt(localStorage.getItem('budget'));
        const functionality = localStorage.getItem('functionality');

        // Validate stored data
        if (!budget || !functionality) {
            resultDiv.innerHTML = "<p>Error: No search criteria found. Please go back and try again.</p>";
            return;
        }

        // Filter cameras
        const recommendations = cameras.filter(camera => 
            camera.price <= budget && 
            (camera.type.toLowerCase() === functionality.toLowerCase() || 
             camera.type.toLowerCase().includes(functionality.toLowerCase()))
        );

        // Display recommendations
        if (recommendations.length > 0) {
            recommendations.forEach(camera => {
                const cameraCard = document.createElement('div');
                cameraCard.classList.add('camera-card');
                cameraCard.innerHTML = `
                    <h3>${camera.name}</h3>
                    <p><strong>Price:</strong> $${camera.price}</p>
                    <p><strong>Type:</strong> ${camera.type}</p>
                    <p><strong>Features:</strong> ${camera.features.join(', ')}</p>
                `;
                resultDiv.appendChild(cameraCard);
            });
        } else {
            resultDiv.innerHTML = `
                <p>No cameras found matching your criteria.</p>
                <p>Try adjusting your budget or functionality.</p>
                <p>Current budget: $${budget}, Functionality: ${functionality}</p>
            `;
        }

        // Back button functionality
        backButton.addEventListener('click', function() {
            // Clear localStorage to reset search
            localStorage.removeItem('budget');
            localStorage.removeItem('functionality');
            window.location.href = 'index.html';
        });
    }
});
