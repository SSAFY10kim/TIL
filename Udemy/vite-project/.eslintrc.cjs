module.exports = {
  root: true,
  env: { browser: true, es2020: true },
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react/jsx-runtime',
    'plugin:react-hooks/recommended',
  ],
  ignorePatterns: ['dist', '.eslintrc.cjs'],
  parserOptions: { ecmaVersion: 'latest', sourceType: 'module' },
  settings: { react: { version: '18.2' } },
  plugins: ['react-refresh'],
  rules: {
    'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
    'prettier/prettier': [{ printWidth: 120 }], // 줄바꿈 120 적용을 위해 해당 부분 추가
    'react/react-in-jsx-scope': 'off',
    'react/jsx-filename-extension': 0,
    'no-unused-vars': 0,
    'react/prop-types': 0,
  },
};
