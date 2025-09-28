document.addEventListener('DOMContentLoaded', function() {
  const overlay = document.getElementById('video-overlay');
  const thumbnail = document.getElementById('youtube-thumbnail');
  const player = document.getElementById('youtube-player');
  const videoContainer = document.getElementById('video-container');
  
  let currentVideoUrl = '';

  function extractYouTubeID(url) {
    if (!url) return null;
    
    const patterns = [
      /(?:youtube\.com\/watch\?v=)([^&\n?#]+)/,
      /(?:youtu\.be\/)([^&\n?#]+)/,
      /(?:youtube\.com\/embed\/)([^&\n?#]+)/
    ];
    
    for (let pattern of patterns) {
      const match = url.match(pattern);
      if (match && match[1]) {
        return match[1];
      }
    }
    return null;
  }

  function loadVideoThumbnail(videoUrl) {
    if (!videoUrl || videoUrl === '{{ sections.demo.video.src }}') {
      showVideoError('No video URL provided');
      return false;
    }

    const videoId = extractYouTubeID(videoUrl);
    if (!videoId) {
      showVideoError('Invalid YouTube URL');
      return false;
    }

    // Try different thumbnail qualities
    const thumbnailUrls = [
      `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`,
      `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`,
      `https://img.youtube.com/vi/${videoId}/mqdefault.jpg`
    ];

    const img = new Image();
    img.onload = function() {
      if (thumbnail) {
        thumbnail.style.backgroundImage = `url('${this.src}')`;
        thumbnail.style.backgroundSize = 'cover';
        thumbnail.style.backgroundPosition = 'center';
      }
      resetVideoState();
    };
    img.onerror = function() {
      const currentIndex = thumbnailUrls.indexOf(this.src);
      if (currentIndex < thumbnailUrls.length - 1) {
        img.src = thumbnailUrls[currentIndex + 1];
      } else {
        showVideoError('Could not load video thumbnail');
      }
    };
    img.src = thumbnailUrls[0];

    currentVideoUrl = videoUrl;
    return true;
  }

  function resetVideoState() {
    if (overlay) overlay.style.display = 'flex';
    if (thumbnail) thumbnail.style.display = 'block';
    if (player) {
      player.classList.add('hidden');
      player.src = '';
    }
    
    // Clear any error messages
    const existingError = videoContainer.querySelector('.video-error-overlay');
    if (existingError) {
      existingError.remove();
    }
  }

  function playVideo() {
    const videoId = extractYouTubeID(currentVideoUrl);
    if (!videoId) {
      showVideoError('Invalid video ID');
      return;
    }

    if (overlay) overlay.style.display = 'none';
    if (thumbnail) thumbnail.style.display = 'none';
    if (player) {
      player.classList.remove('hidden');
      
      const embedUrl = `https://www.youtube.com/embed/${videoId}?autoplay=1&controls=1&rel=0&modestbranding=1&iv_load_policy=3`;
      player.src = embedUrl;
      player.focus();
    }
  }

  function showVideoError(message = 'Video playback failed') {
    // Clear any existing error overlays
    const existingError = videoContainer.querySelector('.video-error-overlay');
    if (existingError) {
      existingError.remove();
    }

    const errorHTML = `
      <div class="video-error-overlay absolute inset-0 z-20 bg-gradient-to-br from-red-50 to-red-100 flex items-center justify-center">
        <div class="text-center">
          <i class="ri-error-warning-line text-6xl text-red-400 mb-4"></i>
          <p class="text-red-600 font-medium">${message}</p>
          <p class="text-red-500 text-sm mt-2">Please check the video URL and try again</p>
        </div>
      </div>
    `;
    
    videoContainer.insertAdjacentHTML('beforeend', errorHTML);
  }

  function setupVideoPlayer() {
    // Get video URL from data attribute
    const videoSrc = videoContainer.dataset.videoUrl;
    
    if (!videoSrc || videoSrc === '{{ sections.demo.video.src }}') {
      showVideoError('No video URL configured');
      return;
    }

    // Load the video thumbnail
    if (loadVideoThumbnail(videoSrc)) {
      // Set up click handler for play button
      if (overlay) {
        overlay.addEventListener('click', function() {
          playVideo();
        });
      }
    }
  }

  // Initialize the video player
  if (videoContainer) {
    setupVideoPlayer();
  } else {
    console.error('Video container not found');
  }
});