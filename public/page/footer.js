import axios from 'axios';

const footer = {
	description: {
	  text: '',
	},
	shortIntro: {
	  text: '',
	},
	copyRight: {
	  text: '© Copyright  {{ years }} | {{ domain }}',
	},
	contact: {
	  phone: {
		name: 'Phone:',
		title: 'Our Phone',
		value: '',
		link: '',
	  },
	  email: {
		name: 'Email:',
		title: 'Our Email',
		value: '',
		link: '',
	  },
	  address: {
		name: 'Address:',
		title: 'Our Address',
		value: '',
		link: '',
	  },
	},
	menu: [
	  {
		name: 'Privacy Policy',
		link: 'privacy-policy',
	  },
	  {
		name: 'Terms & Conditions',
		link: 'terms-and-conditions',
	  },
	],
};
axios.get('https://app.photoresolve.com/getFooterInfo/')
	.then(response => {
	footer.description.text = response.data.description;
	footer.shortIntro.text = response.data.shortIntro;
	footer.contact.phone.value = response.data.phone;
	footer.contact.phone.link = `tel:${response.data.phone}`;
	footer.contact.email.value = response.data.email;
	footer.contact.email.link = `mailto:${response.data.email}`;
	footer.contact.address.value = response.data.address;
	footer.contact.address.link = `https://www.google.com/maps?q=${response.data.address}`;
	})
	.catch(error => {
	console.error(error);
	})

export default footer;
  