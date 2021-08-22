// signup form
if (window.location.href.endsWith('/accounts/signup')) {
	username_input = document.getElementById('id_username')
	email_input = document.getElementById('id_email')
	password1_input = document.getElementById('id_password1')
	password2_input = document.getElementById('id_password2')

	username_input.classList.add('form-control')
	email_input.classList.add('form-control')
	password1_input.classList.add('form-control')
	password2_input.classList.add('form-control')

}else if(window.location.href.endsWith('/accounts/login')){
	username_input = document.getElementById('id_username')
	password_input = document.getElementById('id_password')

	password_input.classList.add('form-control')
	username_input.classList.add('form-control')

} else{
	// home page
	add_item_form = document.getElementById('add_item_form')

	link_input_label = add_item_form.childNodes[3].firstElementChild
	link_input_label.style.display = "none";

	link_input = document.getElementById('id_link')
	link_input.setAttribute('placeholder', 'link to amazon item')
	link_input.classList.add('form-control')
	link_input.classList.add('shadow-none')
}
