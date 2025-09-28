    // FAQ accordion functionality
    document.addEventListener('DOMContentLoaded', function() {
      const faqItems = document.querySelectorAll('.faq-item');
      
      faqItems.forEach(item => {
        const header = item.querySelector('.flex');
        const content = item.querySelector('.faq-content');
        const icon = item.querySelector('.faq-icon i');
        
        // Initially hide content
        content.style.maxHeight = '0';
        content.style.overflow = 'hidden';
        content.style.transition = 'max-height 0.3s ease-out';
        
        header.addEventListener('click', () => {
          const isActive = item.classList.contains('active');
          
          // Close all other FAQ items
          faqItems.forEach(otherItem => {
            if (otherItem !== item) {
              otherItem.classList.remove('active');
              const otherContent = otherItem.querySelector('.faq-content');
              const otherIcon = otherItem.querySelector('.faq-icon i');
              otherContent.style.maxHeight = '0';
              otherIcon.style.transform = 'rotate(0deg)';
            }
          });
          
          // Toggle current item
          if (isActive) {
            item.classList.remove('active');
            content.style.maxHeight = '0';
            icon.style.transform = 'rotate(0deg)';
          } else {
            item.classList.add('active');
            content.style.maxHeight = content.scrollHeight + 'px';
            icon.style.transform = 'rotate(180deg)';
          }
        });
        
        // Add transition for icon rotation
        icon.style.transition = 'transform 0.3s ease';
      });
    });