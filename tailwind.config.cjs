/** @type {import('tailwindcss').Config} */

module.exports = {
	content: [
		"./index.html",
		"./src/**/*.{vue,js,ts,jsx,tsx}",
	],
	darkMode: 'class',
	theme: {
		extend: {
			colors: {
				theme: {
					color: '#4f4747',
					font: 'red'
				}
			},
			fontFamily: {
				'Helvetica': ['Helvetica', 'sans-serif'],
				'Montserrat': ['Montserrat', 'sans-serif'],
			},
		},
	},
	plugins: [],
}
