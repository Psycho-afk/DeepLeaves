// document.addEventListener('DOMContentLoaded', function () {
//     console.log('Document Loaded');
 
//     const carouselElement = document.getElementById('carouselExampleFade');
//     const accordionItems = document.querySelectorAll('.accordion-item');
 
//     if (carouselElement && accordionItems.length > 0) {
//        console.log('Carousel and accordion items found');
 
//        const carousel = new bootstrap.Carousel(carouselElement);
 
//        carouselElement.addEventListener('slide.bs.carousel', function (event) {
//           console.log('Carousel Slide Event');
 
//           const plantId = event.relatedTarget.id;
//           const accordionItemId = 'accordion' + plantId.charAt(plantId.length - 1);
//           const accordionItem = document.getElementById(accordionItemId);
 
//           console.log('Plant ID:', plantId);
//           console.log('Accordion Item ID:', accordionItemId);
 
//           accordionItems.forEach(item => {
//              item.classList.remove('show');
//           });
 
//           if (accordionItem) {
//              accordionItem.classList.add('show');
//              console.log('Accordion Item Shown');
//           }
//        });
//     } else {
//        console.log('Carousel or accordion items not found');
//     }
//  });

document.addEventListener('DOMContentLoaded', function () {
    console.log('Document Loaded');
 
    const accordionItems = document.querySelectorAll('.accordion-item');
 
    if (accordionItems.length > 0) {
       console.log('Accordion items found');
 
       const carouselElement = document.getElementById('carouselExampleFade');
 
       carouselElement.addEventListener('slid.bs.carousel', function () {
          console.log('Carousel Slid Event');
 
          const activeSlide = document.querySelector('.carousel-item.active');
          if (activeSlide) {
             const plantId = activeSlide.id;
             const accordionItemId = 'accordion' + plantId.charAt(plantId.length - 1);
 
             console.log('Active Slide ID:', plantId);
             console.log('Accordion Item ID:', accordionItemId);
 
             accordionItems.forEach(item => {
                item.classList.remove('show');
             });
 
             const accordionItem = document.getElementById(accordionItemId);
             if (accordionItem) {
                accordionItem.classList.add('show');
                console.log('Accordion Item Shown');
             }
          }
       });
    } else {
       console.log('Accordion items not found');
    }
 });
 
 
 
 