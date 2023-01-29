/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
        "./static/src/**/*.js",
        "./node_modules/flowbite/**/*.js"
    ],
    theme: {
    },
    plugins: [
        require("flowbite/plugin")
    ],
}