function toggleFAQ(button) {
    const content = button.nextElementSibling;
    const icon = button.querySelector("i");
    content.classList.toggle("hidden");
    icon.style.transform = content.classList.contains("hidden") ? "rotate(0deg)" : "rotate(180deg)";
  }