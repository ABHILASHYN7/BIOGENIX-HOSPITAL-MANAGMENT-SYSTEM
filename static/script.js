// Particle, confetti, and sparkle animation script
const canvas = document.getElementById('animation-canvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

class Particle {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 5 + 1;
        this.speedX = Math.random() * 3 - 1.5;
        this.speedY = Math.random() * 3 - 1.5;
        this.color = `hsl(${Math.random() * 360}, 70%, 50%)`; // Colorful particles
        this.angle = Math.random() * Math.PI * 2;
        this.distance = Math.random() * 100 + 50;
        this.life = Math.random() * 100 + 50; // Life span for particles
        this.rotation = Math.random() * 360;
    }

    update() {
        this.x += Math.cos(this.angle) * this.speedX;
        this.y += Math.sin(this.angle) * this.speedY;
        this.rotation += Math.random() * 2;
        this.life -= 0.5;

        if (this.x < 0 || this.x > canvas.width) this.speedX = -this.speedX;
        if (this.y < 0 || this.y > canvas.height) this.speedY = -this.speedY;
        if (this.life <= 0) {
            this.reset();
        }

        this.angle += 0.01; // Swirling effect for more dynamism
    }

    reset() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.life = Math.random() * 100 + 50;
        this.rotation = Math.random() * 360;
    }

    draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation * Math.PI / 180);
        ctx.beginPath();
        ctx.arc(0, 0, this.size, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.shadowBlur = 5;
        ctx.shadowColor = this.color;
        ctx.fill();
        ctx.restore();
    }
}

class Confetti {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * -100;
        this.size = Math.random() * 8 + 2;
        this.speedY = Math.random() * 5 + 2;
        this.angle = Math.random() * Math.PI * 2;
        this.speedX = Math.cos(this.angle) * 2;
        this.color = `hsl(${Math.random() * 360}, 80%, 60%)`; // Bright, colorful confetti
        this.opacity = 1;
        this.rotation = Math.random() * 360;
    }

    update() {
        this.y += this.speedY;
        this.x += this.speedX;
        this.rotation += Math.random() * 5;
        this.opacity -= 0.005;
        if (this.opacity <= 0 || this.y > canvas.height) {
            this.y = Math.random() * -100;
            this.x = Math.random() * canvas.width;
            this.opacity = 1;
            this.rotation = Math.random() * 360;
        }
    }

    draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation * Math.PI / 180);
        ctx.fillStyle = `rgba(${this.color.slice(4, -1)}, ${this.opacity})`;
        ctx.fillRect(-this.size / 2, -this.size / 2, this.size, this.size);
        ctx.restore();
    }
}

class Sparkle {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 3 + 1;
        this.speed = Math.random() * 2 + 0.5;
        this.color = `hsl(${Math.random() * 360}, 80%, 70%)`; // Bright, sparkling colors
        this.life = Math.random() * 50 + 30; // Shorter life for sparkles
        this.angle = Math.random() * Math.PI * 2;
        this.rotation = Math.random() * 360;
    }

    update() {
        this.x += Math.cos(this.angle) * this.speed;
        this.y += Math.sin(this.angle) * this.speed;
        this.rotation += Math.random() * 3;
        this.life -= 0.5;

        if (this.x < 0 || this.x > canvas.width || this.y < 0 || this.y > canvas.height || this.life <= 0) {
            this.reset();
        }
    }

    reset() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.life = Math.random() * 50 + 30;
        this.angle = Math.random() * Math.PI * 2;
        this.rotation = Math.random() * 360;
    }

    draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation * Math.PI / 180);
        ctx.beginPath();
        ctx.arc(0, 0, this.size, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.shadowBlur = 15;
        ctx.shadowColor = this.color;
        ctx.fill();
        ctx.restore();
    }
}

const particles = [];
for (let i = 0; i < 200; i++) { // Increased for more vibrancy
    particles.push(new Particle());
}

const confetti = [];
for (let i = 0; i < 100; i++) { // Increased for more vibrancy
    confetti.push(new Confetti());
}

const sparkles = [];
for (let i = 0; i < 150; i++) { // Increased for more vibrancy
    sparkles.push(new Sparkle());
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(particle => {
        particle.update();
        particle.draw();
    });
    confetti.forEach(confettiPiece => {
        confettiPiece.update();
        confettiPiece.draw();
    });
    sparkles.forEach(sparkle => {
        sparkle.update();
        sparkle.draw();
    });
    requestAnimationFrame(animate);
}

animate();

// Resize canvas on window resize
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

// Button hover sound effect and animation burst
const hoverSound = new Audio('/static/hover_sound.mp3'); // Ensure hover_sound.mp3 is in static/
hoverSound.loop = false;

document.querySelectorAll('[data-sound="hover"]').forEach(button => {
    button.addEventListener('mouseover', () => {
        hoverSound.currentTime = 0; // Reset to start
        hoverSound.play().catch(err => console.log("Sound play failed:", err));
        createConfettiBurst(button);
        createSparkleBurst(button);
    });
    button.addEventListener('mouseout', () => {
        hoverSound.pause();
    });
});

// Interactive hero text animation
const heroText = document.querySelector('.hero-text');
heroText.addEventListener('mouseover', () => {
    heroText.style.color = `hsl(${Math.random() * 360}, 80%, 60%)`;
    heroText.style.transform = 'scale(1.1)';
    heroText.style.textShadow = '0 0 20px rgba(255, 235, 59, 1)';
    heroText.style.transition = 'all 0.3s ease';
    createSparkleBurst(heroText);
    createConfettiBurst(heroText);
});
heroText.addEventListener('mouseout', () => {
    heroText.style.color = '#e41b23';
    heroText.style.transform = 'scale(1)';
    heroText.style.textShadow = '3px 3px 8px rgba(0, 0, 0, 0.5), 0 0 20px rgba(255, 235, 59, 0.4)';
});

// Interactive hospital text animation
const hospitalText = document.querySelector('.hospital-text');
if (hospitalText) {
    hospitalText.addEventListener('mouseover', () => {
        hospitalText.style.color = `hsl(${Math.random() * 360}, 80%, 60%)`;
        hospitalText.style.transform = 'scale(1.1)';
        hospitalText.style.textShadow = '0 0 20px rgba(255, 235, 59, 1)';
        hospitalText.style.transition = 'all 0.3s ease';
        createSparkleBurst(hospitalText);
        createConfettiBurst(hospitalText);
    });
    hospitalText.addEventListener('mouseout', () => {
        hospitalText.style.color = '#fff';
        hospitalText.style.transform = 'scale(1)';
        hospitalText.style.textShadow = '2px 2px 6px rgba(0, 0, 0, 0.4), 0 0 15px rgba(255, 235, 59, 0.3)';
    });
});

// Interactive input fields and select for login
document.querySelectorAll('.input-field, select').forEach(input => {
    input.addEventListener('focus', () => {
        createSparkleBurst(input);
    });
    input.addEventListener('blur', () => {
        // No action on blur to maintain simplicity
    });
});

// Interactive dashboard elements
document.querySelectorAll('.dashboard-section, .dashboard-table tr').forEach(element => {
    element.addEventListener('mouseover', () => {
        createSparkleBurst(element);
        if (element.tagName === 'TR') {
            createConfettiBurst(element);
        }
    });
    element.addEventListener('mouseout', () => {
        // No action on mouseout to maintain simplicity
    });
});

function createConfettiBurst(element) {
    const rect = element.getBoundingClientRect();
    const burstCount = 30; // Increased for more vibrant effect
    for (let i = 0; i < burstCount; i++) {
        const confetti = new Confetti();
        confetti.x = rect.left + Math.random() * rect.width;
        confetti.y = rect.top + Math.random() * rect.height;
        confetti.speedY = Math.random() * 12 + 6;
        confetti.speedX = Math.random() * 10 - 5;
        confetti.opacity = 1;
        confetti.size = Math.random() * 15 + 5;
        confetti.color = `hsl(${Math.random() * 360}, 80%, 60%)`; // Bright, colorful confetti
        confetti.rotation = Math.random() * 360;
        confetti.update = function() {
            this.y += this.speedY;
            this.x += this.speedX;
            this.rotation += Math.random() * 10;
            this.opacity -= 0.02;
            if (this.opacity <= 0 || this.y > canvas.height) {
                this.reset();
            }
        };
        confetti.draw(); // Draw immediately for burst effect
        confetti.update(); // Update immediately for burst effect
        confetti.timeout = setTimeout(() => confetti.reset(), 2000); // Reset after 2 seconds
        confetti.push(confetti);
    }
}

function createSparkleBurst(element) {
    const rect = element.getBoundingClientRect();
    const burstCount = 20; // Increased for more vibrant effect
    for (let i = 0; i < burstCount; i++) {
        const sparkle = new Sparkle();
        sparkle.x = rect.left + Math.random() * rect.width;
        sparkle.y = rect.top + Math.random() * rect.height;
        sparkle.speed = Math.random() * 4 + 1;
        sparkle.life = Math.random() * 40 + 20;
        sparkle.color = `hsl(${Math.random() * 360}, 80%, 70%)`; // Bright, sparkling colors
        sparkle.rotation = Math.random() * 360;
        sparkle.update = function() {
            this.x += Math.cos(this.angle) * this.speed;
            this.y += Math.sin(this.angle) * this.speed;
            this.rotation += Math.random() * 5;
            this.life -= 0.5;
            if (this.x < 0 || this.x > canvas.width || this.y < 0 || this.y > canvas.height || this.life <= 0) {
                this.reset();
            }
        };
        sparkle.draw(); // Draw immediately for burst effect
        sparkle.update(); // Update immediately for burst effect
        sparkle.timeout = setTimeout(() => sparkle.reset(), 1500); // Reset after 1.5 seconds
        sparkles.push(sparkle);
    }
}
// ... (existing script.js code remains unchanged) ...

// Ensure particle, confetti, and sparkle animations work with chatbot
function triggerAnimation(type, target) {
    const canvas = document.getElementById('animation-canvas');
    const ctx = canvas.getContext('2d');
    
    if (type === 'confetti') {
        // Simulate confetti burst near the chatbot (bottom-left)
        for (let i = 0; i < 50; i++) {
            createParticle(ctx, target);
        }
    }
}

function createParticle(ctx, target) {
    const rect = document.querySelector(target).getBoundingClientRect();
    const x = rect.left + Math.random() * rect.width;
    const y = rect.top + Math.random() * rect.height;
    const particle = {
        x: x,
        y: y,
        size: Math.random() * 5 + 3,
        speedX: Math.random() * 4 - 2,
        speedY: Math.random() * -4 - 2,
        color: `hsl(${Math.random() * 360}, 70%, 50%)`,
        life: 100
    };
    // Add particle to existing animation loop in script.js (integrate here or modify existing loop)
    particles.push(particle); // Assume particles array exists in script.js
}

// Integrate with existing animation loop (modify script.js accordingly if needed)
// ... (existing script.js code remains unchanged) ...

// Particle, confetti, and sparkle arrays (assume they exist)
