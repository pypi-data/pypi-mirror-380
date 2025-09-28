function toggleMobileMenu() {
    const menu = document.getElementById("mobile-menu");
    const button = document.getElementById("mobile-menu-button");
    const isHidden = menu.classList.contains("hidden");
    menu.classList.toggle("hidden");
    button.setAttribute("aria-expanded", isHidden ? "true" : "false");
  }
  document.getElementById("mobile-menu-button").addEventListener("click", toggleMobileMenu);
  document.querySelectorAll("#mobile-menu a").forEach(link => {
    link.addEventListener("click", toggleMobileMenu);
  });