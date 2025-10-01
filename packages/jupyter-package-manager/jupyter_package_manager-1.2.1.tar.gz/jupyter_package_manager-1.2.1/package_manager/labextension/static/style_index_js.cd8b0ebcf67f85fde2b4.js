"use strict";
(self["webpackChunkjupyter_package_manager"] = self["webpackChunkjupyter_package_manager"] || []).push([["style_index_js"],{

/***/ "./node_modules/css-loader/dist/cjs.js!./style/base.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/base.css ***!
  \**************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/sourceMaps.js */ "./node_modules/css-loader/dist/runtime/sourceMaps.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, `.mljar-packages-manager-sidebar-container {
  height: 99vh;
}
.mljar-packages-manager-sidebar-container::-webkit-scrollbar {
  display: none;
}

.mljar-packages-manager-search-bar-container {
  margin-bottom: 10px;
  margin-right: 0px;
  padding-right: 20px;
  padding-top: 15px;
  padding-bottom: 5px;
  position: sticky;
  top: 38px;
  z-index: 5;
  background: var(--jp-layout-color1);
}

.mljar-packages-manager-install-input,
.mljar-packages-manager-search-bar-input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border: 1px solid var(--jp-border-color2);
  border-radius: 5px;
}

.mljar-packages-manager-install-input:focus,
.mljar-packages-manager-search-bar-input:focus {
  outline: none;
  border: 2px solid var(--jp-ui-font-color1);
}
.mljar-packages-manager-install-input::placeholder,
.mljar-packages-manager-search-bar-input::placeholder {
  color: var(--jp-ui-font-color2);
}

.mljar-packages-manager-header-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 2px solid #ddd;
  position: sticky;
  top: 0;
  z-index: 10;
  background: var(--jp-layout-color1);
  margin-bottom: 0px;
  margin-right: 0px;
  padding-right: 20px;
}

.mljar-packages-manager-header {
  flex: 4;
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--jp-ui-font-color1);
  text-align: left;
  padding-bottom: 8px;
  margin: 0;
}

.mljar-packages-manager-list-container {
  padding-right: 20px;
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow-y: auto;
  position: relative;
}

.mljar-packages-manager-list {
  overflow-y: auto;
  min-height: 0;
  max-height: 85vh;
  list-style: none;
  padding: 0;
  margin: 0;
}

.mljar-packages-manager-sidebar-widget {
  background-color: #ffffff;
  padding: 10px 0px 10px 10px;
  font-family: 'Courier New', Courier, monospace;
}

.mljar-packages-manager-back-button,
.mljar-packages-manager-install-button,
.mljar-packages-manager-refresh-button {
  width: 30px;
  display: flex;
  margin: 2px 1px;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: #0099cc;
  border: none;
  border-radius: 4px;
  padding: 8px 0px;
  cursor: pointer;
  font-size: 0.75rem;
  transition: background-color 0.3s ease;
}

.mljar-packages-manager-back-button {
  width: 70px !important;
  text-align: center;
  padding-right: 4px;
}

.mljar-packages-manager-back-button:hover:not(:disabled),
.mljar-packages-manager-refresh-button:hover:not(:disabled),
.mljar-packages-manager-install-button:hover:not(:disabled) {
  background-color: #0099cc;
  color: #ffffff;
}

.mljar-packages-manager-delete-button {
  visibility: hidden;
  background: none;
  position: relative;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  padding: 4px;
  margin: 5px auto;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #dc3545;
  transition: background-color 0.3s ease;
}

.mljar-packages-manager-refresh-button:disabled,
.mljar-packages-manager-install-button:disabled,
.mljar-packages-manager-back-button:disabled {
  cursor: not-allowed;
}

.mljar-packages-manager-delete-button:hover {
  color: #fff;
  background-color: #dc3545;
  transition: background-color 0.3s ease;
}

.mljar-packages-manager-list-item:hover .mljar-packages-manager-delete-button {
  visibility: visible;
}

.mljar-packages-manager-refresh-icon,
.mljar-packages-manager-install-icon,
.mljar-packages-manager-back-icon {
  display: flex;
  align-items: center;
  width: 15px;
  height: 15px;
}

.mljar-packages-manager-delete-icon {
  display: flex;
  align-items: center;
  width: 20px;
  height: 20px;
}

.mljar-packages-manager-error-icon {
  color: #dc3545;
  width: 15px;
  height: 15px;
}

/* .mljar-packages-manager-info-icon-container {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.mljar-packages-manager-info-icon-container span:first-child {
  display: inline-flex;
  align-items: center;
  color: #0099cc;
  margin: 0px;
  width: 18px;
  height: 18px;
}

.mljar-packages-manager-info-icon-container {
  visibility: hidden;
  width: 150px;
  background-color: #28a745;
  color: white;
  text-align: center;
  border-radius: 4px;
  padding: 5px;
  position: absolute;
  left: -160px;
  top: 100%;
  z-index: 1;
  opacity: 0;
  transition: opacity 0.3s;
  white-space: pre-line;
}

.mljar-packages-manager-info-icon-container:hover {
  visibility: visible;
  opacity: 1;
} */

.mljar-packages-manager-install-form {
  display: flex;
  flex-direction: column;
  margin-right: 0px;
}

.mljar-packages-manager-install-form h4 {
  margin-top: 0px;
  margin-bottom: 4px;
  padding: 0;
}

.mljar-packages-manager-usage-span {
  margin-bottom: 8px;
  text-align: left;
  font-size: 0.8rem;
  padding: 5px 2px;
}

.mljar-packages-manager-error-message {
  color: #dc3545;
  font-weight: bold;
}

.mljar-packages-manager-spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 20px;
}

.mljar-packages-manager-spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border-left-color: #ffffff;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.mljar-packages-manager-list-item {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr 2rem;
  align-items: center;
  min-height: 38px;
  column-gap: 1rem;
  padding-left: 8px;
  padding-right: 8px;
  border-bottom: 1px solid var(--jp-border-color2);
  border-left: 1px solid var(--jp-border-color2);
  border-right: 1px solid var(--jp-border-color2);
  margin-bottom: 0px;
  margin-right: 0px;
  width: 100%;
  box-sizing: border-box;
  background-color: var(--jp-layout-color0);
  font-size: 0.8rem;
  font-weight: 500;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.mljar-packages-manager-list-item:hover {
  background-color: var(--jp-layout-color2);
  cursor: pointer;
}

.mljar-packages-manager-list-item.active {
  background-color: var(--jp-brand-color1);
  color: var(--jp-ui-inverse-font-color1);
}

.mljar-packages-manager-package-name,
.mljar-packages-manager-package-version {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.mljar-packages-manager-package-name {
  font-weight: 600;
}

.mljar-packages-manager-list-header {
  display: grid;
  grid-template-columns: 1fr 1fr 2rem;
  align-items: center;
  font-size: 0.9rem;
  padding-left: 8px;
  padding-right: 8px;
  padding-top: 10px;
  padding-bottom: 10px;
  background-color: var(--jp-layout-color0);
  color: #0099cc;
  border: 1px solid #0099cc;
  border-top-right-radius: 5px;
  border-top-left-radius: 5px;
  font-weight: 800;
}

.mljar-packages-manager-list::-webkit-scrollbar {
  width: 0px;
}

.mljar-packages-manager-list:hover::-webkit-scrollbar {
  width: 10px;
  height: 8px;
}

.mljar-packages-manager-list:hover::-webkit-scrollbar-track {
  background: var(--jp-layout-color2);
  border-radius: 4px;
}

.mljar-packages-manager-list:hover::-webkit-scrollbar-thumb {
  background: var(--jp-layout-color3);
  border-radius: 8px;
  border: 2px solid transparent;
  background-clip: padding-box;
}

/* START */

.mljar-package-manager-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.mljar-package-manager-content {
  background: var(--jp-layout-color1);
  padding: 20px;
  border-radius: 8px;
  width: 600px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.25);
  position: relative;
}

.mljar-package-manager-content h3 {
  font-size: 20px;
}

.mljar-package-manager-modal-close {
  position: absolute;
  top: 10px;
  right: 10px;
  border: none;
  background: transparent;
  font-size: 18px;
  cursor: pointer;
}

/* .mljar-modal-confirm {
  background: #2b7ce9;
  color: white;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
} */

/* .mljar-modal-cancel {
  background: #e0e0e0;
  color: #333;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
} */

.mljar-packages-manager-install-form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.mljar-packages-manager-install-input {
  padding: 6px 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  margin: 1px;
}

.mljar-packages-manager-install-input:focus {
  outline: none;
  border: 2px solid #4a90e2;
  margin: 0px;
}

.mljar-packages-manager-install-logs {
  background: #1e1e1e;
  color: #0f0;
  font-family: monospace;
  font-size: 13px;
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #333;
  max-height: 200px;
  overflow-y: auto;
  white-space: pre-wrap;
  line-height: 1.4;
}

.mljar-packages-manager-install-logs::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

.mljar-packages-manager-install-logs::-webkit-scrollbar-track {
  background: #1e1e1e;
}

.mljar-packages-manager-install-logs::-webkit-scrollbar-thumb {
  background-color: #555;
  border-radius: 4px;
}

.mljar-packages-manager-install-logs::-webkit-scrollbar-thumb:hover {
  background-color: #777;
}

.mljar-packages-manager-install-form-buttons {
  display: flex;
  gap: 8px;
}

.mljar-packages-manager-install-submit-button {
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 6px 14px;
  font-size: 14px;
  cursor: pointer;
  transition: background 0.2s;
}

.mljar-packages-manager-install-submit-button:hover:not(:disabled) {
  background: #43a047;
}

.mljar-packages-manager-install-submit-button:disabled {
  background: #a5d6a7;
  cursor: not-allowed;
}

.mljar-packages-manager-install-message {
  font-size: 14px;
  margin: 0px;
}

.mljar-packages-manager-install-message.error {
  color: #e53935;
}

.mljar-packages-manager-install-message:not(.error) {
  color: #4caf50;
}

.mljar-packages-manager-usage-box {
  background: var(--jp-brand-color3);
  border-left: 4px solid var(--jp-brand-color1);
  padding: 8px 12px;
  border-radius: 4px;
  font-size: 14px;
  color: #333;
}

.mljar-packages-manager-usage-box code {
  background: var(--jp-brand-color4);
  color: var(--jp-brand-color1);
  padding: 2px 4px;
  border-radius: 3px;
  font-family: monospace;
}
.mljar-packages-manager-usage-box strong {
  margin-right: 5px;
}

.mljar-packages-manager-spinner {
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid #fff;
  border-radius: 50%;
  width: 16px;
  height: 16px;
  animation: spin 1s linear infinite;
  margin: auto;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.mljar-packages-manager-result {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
}

.mljar-packages-manager-install-close-button,
.mljar-packages-manager-stop-button {
  background: #e53935;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 6px 14px;
  font-size: 14px;
  cursor: pointer;
  transition: background 0.2s;
}

.mljar-packages-manager-install-close-button:hover,
.mljar-packages-manager-stop-button:hover {
  background: #c62828;
}
`, "",{"version":3,"sources":["webpack://./style/base.css"],"names":[],"mappings":"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","sourcesContent":[".mljar-packages-manager-sidebar-container {\n  height: 99vh;\n}\n.mljar-packages-manager-sidebar-container::-webkit-scrollbar {\n  display: none;\n}\n\n.mljar-packages-manager-search-bar-container {\n  margin-bottom: 10px;\n  margin-right: 0px;\n  padding-right: 20px;\n  padding-top: 15px;\n  padding-bottom: 5px;\n  position: sticky;\n  top: 38px;\n  z-index: 5;\n  background: var(--jp-layout-color1);\n}\n\n.mljar-packages-manager-install-input,\n.mljar-packages-manager-search-bar-input {\n  width: 100%;\n  padding: 8px;\n  box-sizing: border-box;\n  background-color: var(--jp-layout-color1);\n  color: var(--jp-ui-font-color1);\n  border: 1px solid var(--jp-border-color2);\n  border-radius: 5px;\n}\n\n.mljar-packages-manager-install-input:focus,\n.mljar-packages-manager-search-bar-input:focus {\n  outline: none;\n  border: 2px solid var(--jp-ui-font-color1);\n}\n.mljar-packages-manager-install-input::placeholder,\n.mljar-packages-manager-search-bar-input::placeholder {\n  color: var(--jp-ui-font-color2);\n}\n\n.mljar-packages-manager-header-container {\n  display: flex;\n  justify-content: space-between;\n  align-items: flex-end;\n  border-bottom: 2px solid #ddd;\n  position: sticky;\n  top: 0;\n  z-index: 10;\n  background: var(--jp-layout-color1);\n  margin-bottom: 0px;\n  margin-right: 0px;\n  padding-right: 20px;\n}\n\n.mljar-packages-manager-header {\n  flex: 4;\n  font-size: 0.95rem;\n  font-weight: 700;\n  color: var(--jp-ui-font-color1);\n  text-align: left;\n  padding-bottom: 8px;\n  margin: 0;\n}\n\n.mljar-packages-manager-list-container {\n  padding-right: 20px;\n  display: flex;\n  flex-direction: column;\n  height: 100%;\n  overflow-y: auto;\n  position: relative;\n}\n\n.mljar-packages-manager-list {\n  overflow-y: auto;\n  min-height: 0;\n  max-height: 85vh;\n  list-style: none;\n  padding: 0;\n  margin: 0;\n}\n\n.mljar-packages-manager-sidebar-widget {\n  background-color: #ffffff;\n  padding: 10px 0px 10px 10px;\n  font-family: 'Courier New', Courier, monospace;\n}\n\n.mljar-packages-manager-back-button,\n.mljar-packages-manager-install-button,\n.mljar-packages-manager-refresh-button {\n  width: 30px;\n  display: flex;\n  margin: 2px 1px;\n  align-items: center;\n  justify-content: center;\n  gap: 8px;\n  color: #0099cc;\n  border: none;\n  border-radius: 4px;\n  padding: 8px 0px;\n  cursor: pointer;\n  font-size: 0.75rem;\n  transition: background-color 0.3s ease;\n}\n\n.mljar-packages-manager-back-button {\n  width: 70px !important;\n  text-align: center;\n  padding-right: 4px;\n}\n\n.mljar-packages-manager-back-button:hover:not(:disabled),\n.mljar-packages-manager-refresh-button:hover:not(:disabled),\n.mljar-packages-manager-install-button:hover:not(:disabled) {\n  background-color: #0099cc;\n  color: #ffffff;\n}\n\n.mljar-packages-manager-delete-button {\n  visibility: hidden;\n  background: none;\n  position: relative;\n  border: none;\n  border-radius: 4px;\n  cursor: pointer;\n  padding: 4px;\n  margin: 5px auto;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  color: #dc3545;\n  transition: background-color 0.3s ease;\n}\n\n.mljar-packages-manager-refresh-button:disabled,\n.mljar-packages-manager-install-button:disabled,\n.mljar-packages-manager-back-button:disabled {\n  cursor: not-allowed;\n}\n\n.mljar-packages-manager-delete-button:hover {\n  color: #fff;\n  background-color: #dc3545;\n  transition: background-color 0.3s ease;\n}\n\n.mljar-packages-manager-list-item:hover .mljar-packages-manager-delete-button {\n  visibility: visible;\n}\n\n.mljar-packages-manager-refresh-icon,\n.mljar-packages-manager-install-icon,\n.mljar-packages-manager-back-icon {\n  display: flex;\n  align-items: center;\n  width: 15px;\n  height: 15px;\n}\n\n.mljar-packages-manager-delete-icon {\n  display: flex;\n  align-items: center;\n  width: 20px;\n  height: 20px;\n}\n\n.mljar-packages-manager-error-icon {\n  color: #dc3545;\n  width: 15px;\n  height: 15px;\n}\n\n/* .mljar-packages-manager-info-icon-container {\n  position: relative;\n  display: inline-block;\n  cursor: pointer;\n}\n\n.mljar-packages-manager-info-icon-container span:first-child {\n  display: inline-flex;\n  align-items: center;\n  color: #0099cc;\n  margin: 0px;\n  width: 18px;\n  height: 18px;\n}\n\n.mljar-packages-manager-info-icon-container {\n  visibility: hidden;\n  width: 150px;\n  background-color: #28a745;\n  color: white;\n  text-align: center;\n  border-radius: 4px;\n  padding: 5px;\n  position: absolute;\n  left: -160px;\n  top: 100%;\n  z-index: 1;\n  opacity: 0;\n  transition: opacity 0.3s;\n  white-space: pre-line;\n}\n\n.mljar-packages-manager-info-icon-container:hover {\n  visibility: visible;\n  opacity: 1;\n} */\n\n.mljar-packages-manager-install-form {\n  display: flex;\n  flex-direction: column;\n  margin-right: 0px;\n}\n\n.mljar-packages-manager-install-form h4 {\n  margin-top: 0px;\n  margin-bottom: 4px;\n  padding: 0;\n}\n\n.mljar-packages-manager-usage-span {\n  margin-bottom: 8px;\n  text-align: left;\n  font-size: 0.8rem;\n  padding: 5px 2px;\n}\n\n.mljar-packages-manager-error-message {\n  color: #dc3545;\n  font-weight: bold;\n}\n\n.mljar-packages-manager-spinner-container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100%;\n  padding: 20px;\n}\n\n.mljar-packages-manager-spinner {\n  border: 4px solid rgba(0, 0, 0, 0.1);\n  width: 10px;\n  height: 10px;\n  border-radius: 50%;\n  border-left-color: #ffffff;\n  animation: spin 1s linear infinite;\n}\n\n@keyframes spin {\n  to {\n    transform: rotate(360deg);\n  }\n}\n\n.mljar-packages-manager-list-item {\n  flex: 1;\n  display: grid;\n  grid-template-columns: 1fr 1fr 2rem;\n  align-items: center;\n  min-height: 38px;\n  column-gap: 1rem;\n  padding-left: 8px;\n  padding-right: 8px;\n  border-bottom: 1px solid var(--jp-border-color2);\n  border-left: 1px solid var(--jp-border-color2);\n  border-right: 1px solid var(--jp-border-color2);\n  margin-bottom: 0px;\n  margin-right: 0px;\n  width: 100%;\n  box-sizing: border-box;\n  background-color: var(--jp-layout-color0);\n  font-size: 0.8rem;\n  font-weight: 500;\n  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);\n}\n\n.mljar-packages-manager-list-item:hover {\n  background-color: var(--jp-layout-color2);\n  cursor: pointer;\n}\n\n.mljar-packages-manager-list-item.active {\n  background-color: var(--jp-brand-color1);\n  color: var(--jp-ui-inverse-font-color1);\n}\n\n.mljar-packages-manager-package-name,\n.mljar-packages-manager-package-version {\n  overflow: hidden;\n  text-overflow: ellipsis;\n  white-space: nowrap;\n}\n\n.mljar-packages-manager-package-name {\n  font-weight: 600;\n}\n\n.mljar-packages-manager-list-header {\n  display: grid;\n  grid-template-columns: 1fr 1fr 2rem;\n  align-items: center;\n  font-size: 0.9rem;\n  padding-left: 8px;\n  padding-right: 8px;\n  padding-top: 10px;\n  padding-bottom: 10px;\n  background-color: var(--jp-layout-color0);\n  color: #0099cc;\n  border: 1px solid #0099cc;\n  border-top-right-radius: 5px;\n  border-top-left-radius: 5px;\n  font-weight: 800;\n}\n\n.mljar-packages-manager-list::-webkit-scrollbar {\n  width: 0px;\n}\n\n.mljar-packages-manager-list:hover::-webkit-scrollbar {\n  width: 10px;\n  height: 8px;\n}\n\n.mljar-packages-manager-list:hover::-webkit-scrollbar-track {\n  background: var(--jp-layout-color2);\n  border-radius: 4px;\n}\n\n.mljar-packages-manager-list:hover::-webkit-scrollbar-thumb {\n  background: var(--jp-layout-color3);\n  border-radius: 8px;\n  border: 2px solid transparent;\n  background-clip: padding-box;\n}\n\n/* START */\n\n.mljar-package-manager-modal-overlay {\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  bottom: 0;\n  background: rgba(0, 0, 0, 0.5);\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  z-index: 9999;\n}\n\n.mljar-package-manager-content {\n  background: var(--jp-layout-color1);\n  padding: 20px;\n  border-radius: 8px;\n  width: 600px;\n  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.25);\n  position: relative;\n}\n\n.mljar-package-manager-content h3 {\n  font-size: 20px;\n}\n\n.mljar-package-manager-modal-close {\n  position: absolute;\n  top: 10px;\n  right: 10px;\n  border: none;\n  background: transparent;\n  font-size: 18px;\n  cursor: pointer;\n}\n\n/* .mljar-modal-confirm {\n  background: #2b7ce9;\n  color: white;\n  padding: 6px 12px;\n  border: none;\n  border-radius: 4px;\n  cursor: pointer;\n} */\n\n/* .mljar-modal-cancel {\n  background: #e0e0e0;\n  color: #333;\n  padding: 6px 12px;\n  border: none;\n  border-radius: 4px;\n  cursor: pointer;\n} */\n\n.mljar-packages-manager-install-form {\n  display: flex;\n  flex-direction: column;\n  gap: 12px;\n}\n\n.mljar-packages-manager-install-input {\n  padding: 6px 10px;\n  border: 1px solid #ccc;\n  border-radius: 6px;\n  font-size: 14px;\n  margin: 1px;\n}\n\n.mljar-packages-manager-install-input:focus {\n  outline: none;\n  border: 2px solid #4a90e2;\n  margin: 0px;\n}\n\n.mljar-packages-manager-install-logs {\n  background: #1e1e1e;\n  color: #0f0;\n  font-family: monospace;\n  font-size: 13px;\n  padding: 10px;\n  border-radius: 6px;\n  border: 1px solid #333;\n  max-height: 200px;\n  overflow-y: auto;\n  white-space: pre-wrap;\n  line-height: 1.4;\n}\n\n.mljar-packages-manager-install-logs::-webkit-scrollbar {\n  width: 8px;\n  height: 8px;\n}\n\n.mljar-packages-manager-install-logs::-webkit-scrollbar-track {\n  background: #1e1e1e;\n}\n\n.mljar-packages-manager-install-logs::-webkit-scrollbar-thumb {\n  background-color: #555;\n  border-radius: 4px;\n}\n\n.mljar-packages-manager-install-logs::-webkit-scrollbar-thumb:hover {\n  background-color: #777;\n}\n\n.mljar-packages-manager-install-form-buttons {\n  display: flex;\n  gap: 8px;\n}\n\n.mljar-packages-manager-install-submit-button {\n  background: #4caf50;\n  color: white;\n  border: none;\n  border-radius: 6px;\n  padding: 6px 14px;\n  font-size: 14px;\n  cursor: pointer;\n  transition: background 0.2s;\n}\n\n.mljar-packages-manager-install-submit-button:hover:not(:disabled) {\n  background: #43a047;\n}\n\n.mljar-packages-manager-install-submit-button:disabled {\n  background: #a5d6a7;\n  cursor: not-allowed;\n}\n\n.mljar-packages-manager-install-message {\n  font-size: 14px;\n  margin: 0px;\n}\n\n.mljar-packages-manager-install-message.error {\n  color: #e53935;\n}\n\n.mljar-packages-manager-install-message:not(.error) {\n  color: #4caf50;\n}\n\n.mljar-packages-manager-usage-box {\n  background: var(--jp-brand-color3);\n  border-left: 4px solid var(--jp-brand-color1);\n  padding: 8px 12px;\n  border-radius: 4px;\n  font-size: 14px;\n  color: #333;\n}\n\n.mljar-packages-manager-usage-box code {\n  background: var(--jp-brand-color4);\n  color: var(--jp-brand-color1);\n  padding: 2px 4px;\n  border-radius: 3px;\n  font-family: monospace;\n}\n.mljar-packages-manager-usage-box strong {\n  margin-right: 5px;\n}\n\n.mljar-packages-manager-spinner {\n  border: 2px solid rgba(255, 255, 255, 0.3);\n  border-top: 2px solid #fff;\n  border-radius: 50%;\n  width: 16px;\n  height: 16px;\n  animation: spin 1s linear infinite;\n  margin: auto;\n}\n\n@keyframes spin {\n  0% {\n    transform: rotate(0deg);\n  }\n  100% {\n    transform: rotate(360deg);\n  }\n}\n\n.mljar-packages-manager-result {\n  display: flex;\n  flex-direction: column;\n  align-items: flex-start;\n  gap: 12px;\n}\n\n.mljar-packages-manager-install-close-button,\n.mljar-packages-manager-stop-button {\n  background: #e53935;\n  color: white;\n  border: none;\n  border-radius: 6px;\n  padding: 6px 14px;\n  font-size: 14px;\n  cursor: pointer;\n  transition: background 0.2s;\n}\n\n.mljar-packages-manager-install-close-button:hover,\n.mljar-packages-manager-stop-button:hover {\n  background: #c62828;\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./node_modules/css-loader/dist/runtime/api.js":
/*!*****************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/api.js ***!
  \*****************************************************/
/***/ ((module) => {



/*
  MIT License http://www.opensource.org/licenses/mit-license.php
  Author Tobias Koppers @sokra
*/
module.exports = function (cssWithMappingToString) {
  var list = [];

  // return the list of modules as css string
  list.toString = function toString() {
    return this.map(function (item) {
      var content = "";
      var needLayer = typeof item[5] !== "undefined";
      if (item[4]) {
        content += "@supports (".concat(item[4], ") {");
      }
      if (item[2]) {
        content += "@media ".concat(item[2], " {");
      }
      if (needLayer) {
        content += "@layer".concat(item[5].length > 0 ? " ".concat(item[5]) : "", " {");
      }
      content += cssWithMappingToString(item);
      if (needLayer) {
        content += "}";
      }
      if (item[2]) {
        content += "}";
      }
      if (item[4]) {
        content += "}";
      }
      return content;
    }).join("");
  };

  // import a list of modules into the list
  list.i = function i(modules, media, dedupe, supports, layer) {
    if (typeof modules === "string") {
      modules = [[null, modules, undefined]];
    }
    var alreadyImportedModules = {};
    if (dedupe) {
      for (var k = 0; k < this.length; k++) {
        var id = this[k][0];
        if (id != null) {
          alreadyImportedModules[id] = true;
        }
      }
    }
    for (var _k = 0; _k < modules.length; _k++) {
      var item = [].concat(modules[_k]);
      if (dedupe && alreadyImportedModules[item[0]]) {
        continue;
      }
      if (typeof layer !== "undefined") {
        if (typeof item[5] === "undefined") {
          item[5] = layer;
        } else {
          item[1] = "@layer".concat(item[5].length > 0 ? " ".concat(item[5]) : "", " {").concat(item[1], "}");
          item[5] = layer;
        }
      }
      if (media) {
        if (!item[2]) {
          item[2] = media;
        } else {
          item[1] = "@media ".concat(item[2], " {").concat(item[1], "}");
          item[2] = media;
        }
      }
      if (supports) {
        if (!item[4]) {
          item[4] = "".concat(supports);
        } else {
          item[1] = "@supports (".concat(item[4], ") {").concat(item[1], "}");
          item[4] = supports;
        }
      }
      list.push(item);
    }
  };
  return list;
};

/***/ }),

/***/ "./node_modules/css-loader/dist/runtime/sourceMaps.js":
/*!************************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/sourceMaps.js ***!
  \************************************************************/
/***/ ((module) => {



module.exports = function (item) {
  var content = item[1];
  var cssMapping = item[3];
  if (!cssMapping) {
    return content;
  }
  if (typeof btoa === "function") {
    var base64 = btoa(unescape(encodeURIComponent(JSON.stringify(cssMapping))));
    var data = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(base64);
    var sourceMapping = "/*# ".concat(data, " */");
    return [content].concat([sourceMapping]).join("\n");
  }
  return [content].join("\n");
};

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":
/*!****************************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js ***!
  \****************************************************************************/
/***/ ((module) => {



var stylesInDOM = [];
function getIndexByIdentifier(identifier) {
  var result = -1;
  for (var i = 0; i < stylesInDOM.length; i++) {
    if (stylesInDOM[i].identifier === identifier) {
      result = i;
      break;
    }
  }
  return result;
}
function modulesToDom(list, options) {
  var idCountMap = {};
  var identifiers = [];
  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var id = options.base ? item[0] + options.base : item[0];
    var count = idCountMap[id] || 0;
    var identifier = "".concat(id, " ").concat(count);
    idCountMap[id] = count + 1;
    var indexByIdentifier = getIndexByIdentifier(identifier);
    var obj = {
      css: item[1],
      media: item[2],
      sourceMap: item[3],
      supports: item[4],
      layer: item[5]
    };
    if (indexByIdentifier !== -1) {
      stylesInDOM[indexByIdentifier].references++;
      stylesInDOM[indexByIdentifier].updater(obj);
    } else {
      var updater = addElementStyle(obj, options);
      options.byIndex = i;
      stylesInDOM.splice(i, 0, {
        identifier: identifier,
        updater: updater,
        references: 1
      });
    }
    identifiers.push(identifier);
  }
  return identifiers;
}
function addElementStyle(obj, options) {
  var api = options.domAPI(options);
  api.update(obj);
  var updater = function updater(newObj) {
    if (newObj) {
      if (newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap && newObj.supports === obj.supports && newObj.layer === obj.layer) {
        return;
      }
      api.update(obj = newObj);
    } else {
      api.remove();
    }
  };
  return updater;
}
module.exports = function (list, options) {
  options = options || {};
  list = list || [];
  var lastIdentifiers = modulesToDom(list, options);
  return function update(newList) {
    newList = newList || [];
    for (var i = 0; i < lastIdentifiers.length; i++) {
      var identifier = lastIdentifiers[i];
      var index = getIndexByIdentifier(identifier);
      stylesInDOM[index].references--;
    }
    var newLastIdentifiers = modulesToDom(newList, options);
    for (var _i = 0; _i < lastIdentifiers.length; _i++) {
      var _identifier = lastIdentifiers[_i];
      var _index = getIndexByIdentifier(_identifier);
      if (stylesInDOM[_index].references === 0) {
        stylesInDOM[_index].updater();
        stylesInDOM.splice(_index, 1);
      }
    }
    lastIdentifiers = newLastIdentifiers;
  };
};

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/insertBySelector.js":
/*!********************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/insertBySelector.js ***!
  \********************************************************************/
/***/ ((module) => {



var memo = {};

/* istanbul ignore next  */
function getTarget(target) {
  if (typeof memo[target] === "undefined") {
    var styleTarget = document.querySelector(target);

    // Special case to return head of iframe instead of iframe itself
    if (window.HTMLIFrameElement && styleTarget instanceof window.HTMLIFrameElement) {
      try {
        // This will throw an exception if access to iframe is blocked
        // due to cross-origin restrictions
        styleTarget = styleTarget.contentDocument.head;
      } catch (e) {
        // istanbul ignore next
        styleTarget = null;
      }
    }
    memo[target] = styleTarget;
  }
  return memo[target];
}

/* istanbul ignore next  */
function insertBySelector(insert, style) {
  var target = getTarget(insert);
  if (!target) {
    throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
  }
  target.appendChild(style);
}
module.exports = insertBySelector;

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/insertStyleElement.js":
/*!**********************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/insertStyleElement.js ***!
  \**********************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function insertStyleElement(options) {
  var element = document.createElement("style");
  options.setAttributes(element, options.attributes);
  options.insert(element, options.options);
  return element;
}
module.exports = insertStyleElement;

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js":
/*!**********************************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js ***!
  \**********************************************************************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {



/* istanbul ignore next  */
function setAttributesWithoutAttributes(styleElement) {
  var nonce =  true ? __webpack_require__.nc : 0;
  if (nonce) {
    styleElement.setAttribute("nonce", nonce);
  }
}
module.exports = setAttributesWithoutAttributes;

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/styleDomAPI.js":
/*!***************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/styleDomAPI.js ***!
  \***************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function apply(styleElement, options, obj) {
  var css = "";
  if (obj.supports) {
    css += "@supports (".concat(obj.supports, ") {");
  }
  if (obj.media) {
    css += "@media ".concat(obj.media, " {");
  }
  var needLayer = typeof obj.layer !== "undefined";
  if (needLayer) {
    css += "@layer".concat(obj.layer.length > 0 ? " ".concat(obj.layer) : "", " {");
  }
  css += obj.css;
  if (needLayer) {
    css += "}";
  }
  if (obj.media) {
    css += "}";
  }
  if (obj.supports) {
    css += "}";
  }
  var sourceMap = obj.sourceMap;
  if (sourceMap && typeof btoa !== "undefined") {
    css += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))), " */");
  }

  // For old IE
  /* istanbul ignore if  */
  options.styleTagTransform(css, styleElement, options.options);
}
function removeStyleElement(styleElement) {
  // istanbul ignore if
  if (styleElement.parentNode === null) {
    return false;
  }
  styleElement.parentNode.removeChild(styleElement);
}

/* istanbul ignore next  */
function domAPI(options) {
  if (typeof document === "undefined") {
    return {
      update: function update() {},
      remove: function remove() {}
    };
  }
  var styleElement = options.insertStyleElement(options);
  return {
    update: function update(obj) {
      apply(styleElement, options, obj);
    },
    remove: function remove() {
      removeStyleElement(styleElement);
    }
  };
}
module.exports = domAPI;

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/styleTagTransform.js":
/*!*********************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/styleTagTransform.js ***!
  \*********************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function styleTagTransform(css, styleElement) {
  if (styleElement.styleSheet) {
    styleElement.styleSheet.cssText = css;
  } else {
    while (styleElement.firstChild) {
      styleElement.removeChild(styleElement.firstChild);
    }
    styleElement.appendChild(document.createTextNode(css));
  }
}
module.exports = styleTagTransform;

/***/ }),

/***/ "./style/base.css":
/*!************************!*\
  !*** ./style/base.css ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/styleDomAPI.js */ "./node_modules/style-loader/dist/runtime/styleDomAPI.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/insertBySelector.js */ "./node_modules/style-loader/dist/runtime/insertBySelector.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js */ "./node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/insertStyleElement.js */ "./node_modules/style-loader/dist/runtime/insertStyleElement.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/styleTagTransform.js */ "./node_modules/style-loader/dist/runtime/styleTagTransform.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./base.css */ "./node_modules/css-loader/dist/cjs.js!./style/base.css");

      
      
      
      
      
      
      
      
      

var options = {};

options.styleTagTransform = (_node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5___default());
options.setAttributes = (_node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3___default());

      options.insert = _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2___default().bind(null, "head");
    
options.domAPI = (_node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1___default());
options.insertStyleElement = (_node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4___default());

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__["default"], options);




       /* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__["default"] && _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__["default"].locals ? _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__["default"].locals : undefined);


/***/ }),

/***/ "./style/index.js":
/*!************************!*\
  !*** ./style/index.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _base_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./base.css */ "./style/base.css");



/***/ })

}]);
//# sourceMappingURL=style_index_js.cd8b0ebcf67f85fde2b4.js.map