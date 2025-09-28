const hamburgerBtn = document.querySelector('.hamburger');
const mobileMenu = document.querySelector('.mobile-menu');
hamburgerBtn.addEventListener('click', () => {
  hamburgerBtn.classList.toggle('active');
  if (mobileMenu.classList.contains('hidden')) {
    mobileMenu.classList.remove('hidden');
    hamburgerBtn.setAttribute('aria-expanded', 'true');
  } else {
    mobileMenu.classList.add('hidden');
    hamburgerBtn.setAttribute('aria-expanded', 'false');
  }
});
function closeMobileMenu() {
  hamburgerBtn.classList.remove('active');
  mobileMenu.classList.add('hidden');
  hamburgerBtn.setAttribute('aria-expanded', 'false');
}
