$(document).ready(function()
{
    function updateHelpBlock(container, input) {
	var helpBlock = container.find(".help-block");

	if (input.isValid && helpBlock.length)
	    $(helpBlock[0]).remove();
	else if (!input.isValid) {
	    helpBlock = (helpBlock.length ? $(helpBlock[0]) : $(container.append("<span class='help-block'></span>").find(".help-block")[0]))
	    helpBlock.text(input.errorMessage);
	}
    }

    function updateInputsDisplay(inputs) {
	$.each(inputs, function() {
	    var input = $(this.elementId);
	    var parent = input.parent();

	    if (input.val().length)
		this.hasBeenModified = true;
	    if (this.hasBeenModified)
		updateHelpBlock(parent, this);
	    if (this.isValid) {
		parent.removeClass("has-error");
		parent.addClass("has-success");
	    }
	    else if (this.hasBeenModified) {
		parent.removeClass("has-success");
		parent.addClass("has-error");
	    }
	});
    }

    function checkUsername(usernameId) {
	var regex = /^[A-Za-z0-9@.+-_]+$/;
	return (regex.test($(usernameId).val()));
    }

    function checkEmail(emailId) {
	var regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return (regex.test($(emailId).val()));
    }

    function checkPassword(passwordId) {
	return ($(passwordId).val().length > 7);
    }

    function checkPasswordConfirm(passwordId, passwordConfirmId) {
	return ($(passwordId).val().length && $(passwordId).val() === $(passwordConfirmId).val());
    }

    function checkFormValidity(inputs) {
	inputs.username.isValid = checkUsername(inputs.username.elementId);
	inputs.email.isValid = checkEmail(inputs.email.elementId);
	inputs.password.isValid = checkPassword(inputs.password.elementId);
	inputs.passwordConfirm.isValid = checkPasswordConfirm(inputs.password.elementId, inputs.passwordConfirm.elementId);
	updateInputsDisplay(inputs);
	if (inputs.username.isValid && inputs.email.isValid && inputs.password.isValid && inputs.passwordConfirm.isValid)
	    $('#submit-button').removeAttr('disabled');
	else
	    $('#submit-button').attr('disabled', 'disabled');
    }

    var inputs = {
	username: {elementId: "#id_username", errorMessage: "Nom d'utilisateur invalide. Le nom d'utilisateur ne peut contenir que des lettres, nombres et les caractères « @ », « . », « + », « - » et « _ »"},
	email: {elementId: "#id_email", errorMessage: "Adresse email invalide"},
	password: {elementId: "#id_password", errorMessage: "Le mot de passe doit contenir au moins 8 caractères"},
	passwordConfirm: {elementId: "#id_password_confirm", errorMessage: "Confirmation du mot de passe invalide"}
    };

    $('#submit-button').attr('disabled', 'disabled');
    $('#id_username, #id_email, #id_password, #id_password_confirm').keyup(function()
									   {
									       checkFormValidity(inputs);
									   });
});
