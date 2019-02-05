(()=>{


	let projects = document.querySelectorAll(".promoText_Projects");
	let articles = document.querySelectorAll(".articles");
	console.log(articles);
	console.log(projects);

projects[0].addEventListener("click", function()
	{
		articles[0].classList.toggle("deleteArticles");
	});


projects[1].addEventListener("click", function()
	{
		articles[1].classList.toggle("deleteArticles").style.transitionDuration = "1s";
	});


projects[2].addEventListener("click", function()
	{
		articles[2].classList.toggle("deleteArticles");
	});


projects[3].addEventListener("click", function()
	{
		articles[3].classList.toggle("deleteArticles");
	});


	// projects.forEach(show => show.addEventListener("click",showArticles));

	var parallax = document.querySelector(".parallax");

	window.addEventListener("scroll", function ()
	{

		let offset = window.pageYOffset;
		console.log("Offset: " + offset);
		console.log(parallax);
		parallax.style.backgroundPositionY = offset * 0.1 +"px";
	});


	})();