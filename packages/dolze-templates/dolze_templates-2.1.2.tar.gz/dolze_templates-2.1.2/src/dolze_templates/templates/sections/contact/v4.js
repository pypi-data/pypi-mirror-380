document.getElementById("contactForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const inputs = this.querySelectorAll("input[required], textarea[required]");
    let allFilled = true;
    inputs.forEach((input) => {
      if (!input.value.trim()) allFilled = false;
    });
    if (allFilled) {
      document.getElementById("successDialog").classList.remove("hidden");
      this.reset();
    }
  });