let camera, scene, renderer, arController, currentModel;
const arContainer = document.getElementById('ar-container');
const cameraSelect = document.getElementById('camera-select');
const startARButton = document.getElementById('start-ar-button');
const infoDiv = document.getElementById('info');

// **Step 1: Camera Selection and Initialization**
async function initCameraSelection() {
    try {
        const devices = await navigator.mediaDevices.enumerateDevices();
        const videoInputDevices = devices.filter(device => device.kind === 'videoinput');
        
        if (videoInputDevices.length === 0) {
            throw new Error('No video cameras found.');
        }
        
        videoInputDevices.forEach((device, index) => {
            const option = document.createElement('option');
            option.value = device.deviceId;
            option.text = device.label || `Camera ${index + 1}`;
            cameraSelect.appendChild(option);
        });
        
        // Select the first camera by default
        cameraSelect.value = videoInputDevices[0].deviceId;
        
        cameraSelect.addEventListener('change', async () => {
            await initializeCamera(cameraSelect.value);
        });
        
        startARButton.addEventListener('click', async () => {
            if (camera) {
                await startARExperience();
            } else {
                alert('Please select a camera.');
            }
        });
    } catch (error) {
        console.error('Error accessing cameras:', error);
    }
}

async function initializeCamera(deviceId) {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: {
                deviceId: deviceId
            }
        });
        camera = new THREE.Camera(stream);
    } catch (error) {
        console.error('Error initializing camera:', error);
    }
}

// **Step 2: AR Scene Setup with Three.js and WebXR**
async function startARExperience() {
    try {
        // **WebXR Setup**
        const session = await navigator.xr.requestSession('immersive-ar', {
            requiredFeatures: ['local-floor', 'bounded-floor', 'plane-detection', 'hand-tracking'],
            optionalFeatures: ['hand-tracking']
        });
        
        // **Three.js Scene Setup**
        scene = new THREE.Scene();
        renderer = new THREE.Renderer({
            canvas: document.createElement('canvas'),
            context: canvas.getContext('2d')
        });
        arController = new THREE.WebXRController(session, renderer, camera);
        
        // **ARCore Integration (on Android)**
        if (window.ARCore) { 
            const arCoreSession = new ARCore.Web_SDK.Session();
            await arCoreSession.init();
            // Integrate ARCore's plane detection with Three.js (simplified example)
            //...
        }
        
        // **Load 3D Models (example)**
        const loader = new THREE.GLTFLoader();
        loader.load('models/CPU.glb', (gltf) => {
            scene.add(gltf.scene);
            currentModel = gltf.scene;
        });
        
        // **Event Handling for Marker Detection, Rotation, and Zooming**
        setupMarkerEvents();
        setupRotationAndZooming();
        
        arContainer.appendChild(renderer.domElement);
        infoDiv.style.display = 'none';
        cameraSelect.style.display = 'none';
        startARButton.style.display = 'none';
        arContainer.style.display = 'block';
    } catch (error) {
        console.error('Error starting AR experience:', error);
    }
}

// **Event Handling for Marker Detection, Rotation, and Zooming (simplified)**
function setupMarkerEvents() {
    // TO DO: Implement marker detection logic using WebXR and Three.js
}

function setupRotationAndZooming() {
    // TO DO: Implement rotation and zooming logic using Three.js event handlers
    // Example:
    document.addEventListener('wheel', (event) => {
        if (currentModel) {
            // Zoom logic (simplified)
            currentModel.scale.y += event.deltaY * 0.01;
            currentModel.scale.x += event.deltaY * 0.01;
            currentModel.scale.z += event.deltaY * 0.01;
        }
    });
}

// **Initialization**
initCameraSelection();