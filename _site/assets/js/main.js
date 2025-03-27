// 示例 1：点击按钮显示/隐藏元素
document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.getElementById('toggle-button');
  const targetElement = document.getElementById('target-element');

  if (toggleButton && targetElement) {
    toggleButton.addEventListener('click', function () {
      targetElement.style.display = targetElement.style.display === 'none'? 'block' : 'none';
    });
  }
});

// 示例 2：给链接添加点击事件
const links = document.querySelectorAll('a');
links.forEach(function (link) {
  link.addEventListener('click', function (event) {
    // 在这里可以添加点击链接时的自定义逻辑，比如阻止默认行为等
    // event.preventDefault(); 
    console.log('链接被点击了：', this.href);
  });
});

// 示例 3：实现一个简单的轮播图效果（简化版）
const slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function showSlide() {
  slides.forEach((slide, index) => {
    if (index === currentSlide) {
      slide.style.display = 'block';
    } else {
      slide.style.display = 'none';
    }
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % slides.length;
  showSlide();
}

setInterval(nextSlide, 3000); // 每 3 秒切换一次幻灯片

showSlide();
