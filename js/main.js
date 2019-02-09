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
		articles[1].classList.toggle("deleteArticles");
	});


projects[2].addEventListener("click", function()
	{
		articles[2].classList.toggle("deleteArticles");

	});


projects[3].addEventListener("click", function()
	{
		articles[3].classList.toggle("deleteArticles");

	});

projects[4].addEventListener("click", function()
	{
		articles[4].classList.toggle("deleteArticles");

	});



	// projects.forEach(show => show.addEventListener("click",showArticles));

// 	var elmnt = document.getElementsByClassName("articles");
// elmnt.scrollIntoView();
// 	});


	})();






