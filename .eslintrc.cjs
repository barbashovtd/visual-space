module.exports = {
  env: { node: true, },
  extends: [
    // add more generic rulesets here, such as:
    // 'eslint:recommended',
    'plugin:vue/vue3-recommended',
    "prettier",
  ],
  rules: {
    // override/add rules settings here, such as:
    // 'vue/no-unused-vars': 'error'
    "unused-imports/no-unused-imports": "off",
    "no-unused-vars": "off"
  }
}
