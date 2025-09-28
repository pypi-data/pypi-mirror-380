document.getElementById("subscribeForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const emailInput = this.querySelector('input[type="email"]');
    const email = emailInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email && emailRegex.test(email)) {
      document.getElementById("subscribeDialog").classList.remove("hidden");
      this.reset();
    }
  });