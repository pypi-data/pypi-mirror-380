    // Video player
    document.addEventListener('DOMContentLoaded', function() {
        const videoContainer = document.getElementById("video-container");
        const originalVideoHTML = videoContainer.innerHTML;
      
        function setupVideoPlayer() {
          const overlay = document.getElementById("video-overlay");
          const videoElement = document.getElementById("demo-video");
          const sourceEl = videoElement ? videoElement.querySelector("source") : null;
          overlay.addEventListener("click", function() {
            overlay.style.display = "none";
            if (sourceEl) {
              const videoSrc = sourceEl.getAttribute("src");
              if (videoSrc.includes("youtube.com") || videoSrc.includes("youtu.be")) {
                let embedUrl = videoSrc;
                if (videoSrc.includes("watch?v=")) {
                  embedUrl = videoSrc.replace("watch?v=", "embed/");
                }
                embedUrl += (embedUrl.includes("?") ? "&" : "?") + "autoplay=1&controls=1";
                const ytContainer = document.createElement("div");
                ytContainer.id = "youtube-player";
                ytContainer.className = videoElement.className;
                videoElement.parentNode.replaceChild(ytContainer, videoElement);
                if (typeof YT === 'undefined' || typeof YT.Player === 'undefined') {
                  let tag = document.createElement('script');
                  tag.src = "https://www.youtube.com/iframe_api";
                  let firstScriptTag = document.getElementsByTagName('script')[0];
                  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
                  window.onYouTubeIframeAPIReady = function() {
                    createYTPlayer(ytContainer.id, embedUrl);
                  };
                } else {
                  createYTPlayer(ytContainer.id, embedUrl);
                }
              } else {
                videoElement.play();
                videoElement.addEventListener("ended", function() {
                  resetVideo();
                });
              }
            }
          });
        }
      
        function createYTPlayer(elementId, embedUrl) {
          new YT.Player(elementId, {
            videoId: extractYouTubeID(embedUrl),
            playerVars: {
              autoplay: 1,
              controls: 1
            },
            events: {
              'onStateChange': function(event) {
                if (event.data === YT.PlayerState.ENDED) {
                  resetVideo();
                }
              }
            }
          });
        }
      
        function extractYouTubeID(url) {
          const regExp = /embed\/([^\?&"'>]+)/;
          const match = url.match(regExp);
          return (match && match[1]) ? match[1] : '';
        }
      
        function resetVideo() {
          videoContainer.innerHTML = originalVideoHTML;
          setupVideoPlayer();
        }
      
        setupVideoPlayer();
      });
    
