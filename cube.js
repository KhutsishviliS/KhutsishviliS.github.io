document.addEventListener('DOMContentLoaded', function() {
    const cube = document.querySelector('.cube');
    let isDragging = false;
    let startX = 0;
    let currentRotation = 0;

    function startRotating(e) {
        isDragging = true;
        startX = e.clientX || e.touches[0].clientX;
        cube.style.animation = 'none';
    }

    function rotate(e) {
        if (!isDragging) return;
        
        e.preventDefault();
        const x = e.clientX || e.touches[0].clientX;
        const deltaX = x - startX;
        
        // Convert the movement to rotation degrees (adjust sensitivity with the division factor)
        const newRotation = currentRotation + (deltaX / 2);
        
        // Apply the rotation only around the Y axis
        cube.style.transform = `rotateY(${newRotation}deg)`;
    }

    function stopRotating(e) {
        if (!isDragging) return;
        
        isDragging = false;
        // Store the final rotation
        const style = window.getComputedStyle(cube);
        const matrix = new WebKitCSSMatrix(style.transform);
        currentRotation = Math.round(Math.atan2(matrix.m13, matrix.m11) * (180/Math.PI));
        
        // Resume animation
        cube.style.animation = 'cube-rotate 20s infinite linear';
    }

    // Mouse events
    cube.addEventListener('mousedown', startRotating);
    document.addEventListener('mousemove', rotate);
    document.addEventListener('mouseup', stopRotating);

    // Touch events
    cube.addEventListener('touchstart', (e) => {
        e.preventDefault();
        startRotating(e.touches[0]);
    });
    
    document.addEventListener('touchmove', (e) => {
        rotate(e.touches[0]);
    });
    
    document.addEventListener('touchend', stopRotating);
});