

  
    // Modal functionality
    const signupModal = document.getElementById('signupModal');
    const successModal = document.getElementById('successModal');
    const closeModalBtn = document.getElementById('closeModal');
    const closeSuccessModalBtn = document.getElementById('closeSuccessModal');
    const signupForm = document.getElementById('signupForm');
    const headerGetStartedBtn = document.getElementById('headerGetStarted');
    const getStartedBtns = document.querySelectorAll('.get-started-btn');
    const watchDemoBtn = document.getElementById('watchDemoBtn');
    function openSignupModal() {
      signupModal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
      if (!mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
        hamburgerBtn.classList.remove('active');
        hamburgerBtn.setAttribute('aria-expanded', 'false');
      }
    }
    headerGetStartedBtn.addEventListener('click', function(e) {
      e.preventDefault();
      openSignupModal();
    });
    getStartedBtns.forEach(btn => {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        openSignupModal();
      });
    });
    if (watchDemoBtn) {
      watchDemoBtn.addEventListener('click', function(e) {
        e.preventDefault();
        const demoSection = document.getElementById('demo');
        demoSection.scrollIntoView({ behavior: 'smooth' });
      });
    }
    closeModalBtn.addEventListener('click', function() {
      signupModal.classList.add('hidden');
      document.body.style.overflow = 'auto';
    });
    window.addEventListener('click', function(e) {
      if (e.target === signupModal) {
        signupModal.classList.add('hidden');
        document.body.style.overflow = 'auto';
      }
      if (e.target === successModal) {
        successModal.classList.add('hidden');
        document.body.style.overflow = 'auto';
      }
    });
    signupForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const phone = document.getElementById('phone').value;
      signupForm.reset();
      signupModal.classList.add('hidden');
      successModal.classList.remove('hidden');
    });