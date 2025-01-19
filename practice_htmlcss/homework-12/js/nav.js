// В результате действия данного скрипта,
// по клику на кнопку с id="navBtn"
// элемент с id="mainNav" будет плавно, появляться, если он скрыт
// и скрываться, если он виден.

// Для того, чтобы этот скрипт работал корректно,
// у элемента с id="mainNav" (в вашей верстке это будет блок навигации)
// изначально должен быть класс nav-hidden со следующими свойствами:
// .nav-hidden {
//	 height: 0;
// }

// также у блока навигации обязательно должны быть свойства:
// .main-nav {
//	 overflow: hidden;
//   transition: height 2s;
// }

// точка перехода блока навигации в скрытое || развернутое состояние в данном проекте 1024px, 
// если блок навигации должен скрываться || показываться  при другой ширине экрана, 
// нужно изменить значение переменной point


function navToggle() {

	const navBtn = document.getElementById('navBtn');
	const mainNav = document.getElementById('mainNav');
	const point = 685;

	navBtn.onclick = function () {		
		let heightNav = mainNav.firstElementChild.offsetHeight;		
		if (mainNav.classList.contains('nav-hidden')) {
			mainNav.classList.remove('nav-hidden');
			mainNav.style.height = heightNav + 'px';
		} else {
			mainNav.classList.add('nav-hidden');
			mainNav.style.height = 0;
		}
	}

	window.addEventListener("resize", resizeHandler, false);

	function resizeHandler() {
		let heightNav = mainNav.firstElementChild.offsetHeight;
		if (document.documentElement.clientWidth >= point) {
			mainNav.style.height = 'auto';
		} else {
			if (mainNav.classList.contains('nav-hidden')) {
				mainNav.style.height = 0;
			} else {
				mainNav.style.height = heightNav + 'px';
			}
		}
	}
}

navToggle();