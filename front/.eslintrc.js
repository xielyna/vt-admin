module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/essential',
    '@vue/standard',
    '@vue/typescript/recommended'
  ],
  parserOptions: {
    ecmaVersion: 2020
  },
  rules: {
    '@typescript-eslint/ban-types': 'off',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/member-delimiter-style': [
      'error',
      {
        multiline: {
          delimiter: 'none'
        },
        singleline: {
          delimiter: 'comma'
        }
      }
    ],
    '@typescript-eslint/no-explicit-any': 'off',
    '@typescript-eslint/no-var-requires': 'off',
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'space-before-function-paren': ['error', 'never'],
    'vue/array-bracket-spacing': 'error',
    'vue/arrow-spacing': 'error',
    'vue/block-spacing': 'error',
    'vue/brace-style': 'error',
    'vue/camelcase': 'error',
    'vue/comma-dangle': 'error',
    'vue/component-name-in-template-casing': ['error', 'kebab-case'],
    'vue/eqeqeq': 'error',
    'vue/key-spacing': 'error',
    'vue/match-component-file-name': 'error',
    'vue/object-curly-spacing': 'error'
  },
  overrides: [
    {
      files: [
        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)'
      ],
      env: {
        jest: true
      }
    }
  ]
}
// module.exports = {
//   root: true,
//   env: {
//     browser: true,
//     node: true,
//     es6: true
//   },
//   extends: [
//     'plugin:vue/recommended',
//     '@vue/typescript',
//     'plugin:prettier/recommended',
//     'prettier/vue'
//   ],
//   rules: {
//     curly: 'error',
//     'prefer-const': 'error',
//     'no-unused-vars': 0,
//     'vue/no-v-html': 0,
//     'vue/order-in-components': 2,
//     quotes: [1, 'single'], //使用单引号，提示是警告
//     quotes: [0, 'double'], //使用双引号，关闭
//     'vue/max-attributes-per-line': [
//       0,
//       {
//         singleline: 2,
//         multiline: {
//           max: 1,
//           allowFirstLine: false
//         }
//       }
//     ],
//     'lines-between-class-members': [
//       'error',
//       'always',
//       {
//         exceptAfterSingleLine: true
//       }
//     ],
//     'no-extra-semi': 0,
//     'vue/html-indent': [
//       0,
//       'tab',
//       {
//         attribute: 1,
//         baseIndent: 1,
//         closeBracket: 0,
//         alignAttributesVertically: true,
//         ignores: []
//       }
//     ],
//     'vue/html-closing-bracket-newline': 0,
//     'vue/html-self-closing': 0,
//     'vue/singleline-html-element-content-newline': [
//       'error',
//       {
//         ignoreWhenNoAttributes: true,
//         ignoreWhenEmpty: true
//       }
//     ]
//   }
// }
