  // Pricing toggle
  const pricingToggle = document.getElementById('pricing-toggle');
  const monthlyPrices = document.querySelectorAll('.monthly-price');
  const yearlyPrices = document.querySelectorAll('.yearly-price');
  const billingPeriods = document.querySelectorAll('.billing-period');
  pricingToggle.addEventListener('change', function() {
    if (this.checked) {
      monthlyPrices.forEach(price => price.classList.add('hidden'));
      yearlyPrices.forEach(price => price.classList.remove('hidden'));
      billingPeriods.forEach(period => period.textContent = '/month, billed annually');
    } else {
      monthlyPrices.forEach(price => price.classList.remove('hidden'));
      yearlyPrices.forEach(price => price.classList.add('hidden'));
      billingPeriods.forEach(period => period.textContent = '/month');
    }
  });