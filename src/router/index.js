import { createRouter, createWebHistory } from "vue-router";
const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	scrollBehavior(to, from, savedPosition) {
		//window.scrollTo(0, 0);
		console.log(savedPosition)
	},
	routes: [
		{
			path: "/",
			name: "home",
			component: () => import("../views/HomeView.vue"),
			meta: {
				title: "Home",
			},
		},
		{
			path: "/service/e-commerce",
			name: "service-fashion",
			component: () => import("../components/section/service/fashion.vue"),
			meta: {
				title: "Fashion",
			},
		},
		{
			path: "/service/product",
			name: "service-product",
			component: () => import("../components/section/service/product.vue"),
			meta: {
				title: "Product",
			},
		},
		{
			path: "/service/jewelry",
			name: "service-jewelry",
			component: () => import("../components/section/service/jewelry.vue"),
			meta: {
				title: "jewelry",
			},
		},
		{
			path: "/service/others",
			name: "service-others",
			component: () => import("../components/section/service/others.vue"),
			meta: {
				title: "Others Services",
			},
		},
		{
			path: "/contact",
			name: "contact",
			component: () => import("../views/contactView.vue"),
			meta: {
				title: "Contact",
			},
		},
		{
			path: "/pricing",
			name: "prices",
			component: () => import("../views/pricesView.vue"),
			meta: {
				title: "Pricing",
			},
		},
		{
			path: "/portfolio",
			name: "portfolio",
			component: () => import("../views/portfolioView.vue"),
			meta: {
				title: "Portfolio",
			},
		},
		{
			path: "/terms-and-conditions",
			name: "terms-and-conditions",
			component: () => import("../views/termAndConditionsView.vue"),
			meta: {
				title: "Terms And Conditionso",
			},
		},
		{
			path: "/privacy-policy",
			name: "privacy-policy",
			component: () => import("../views/privacyPolicyView.vue"),
			meta: {
				title: "Privacy Policy",
			},
		}
	],
});


router.beforeEach((to, from, next) => {

	const appname = 'Photoresolve.com';
	const titleWrapper = to.meta.title
		? `${to.meta.title} || ${appname}`
		: appname;

	if (titleWrapper) document.title = titleWrapper;
	next();

});

export default router;
