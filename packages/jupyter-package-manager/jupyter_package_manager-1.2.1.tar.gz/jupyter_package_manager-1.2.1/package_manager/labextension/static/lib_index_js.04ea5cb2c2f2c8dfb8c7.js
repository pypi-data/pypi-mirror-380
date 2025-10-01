"use strict";
(self["webpackChunkjupyter_package_manager"] = self["webpackChunkjupyter_package_manager"] || []).push([["lib_index_js"],{

/***/ "./lib/components/installButton.js":
/*!*****************************************!*\
  !*** ./lib/components/installButton.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   InstallButton: () => (/* binding */ InstallButton)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../contexts/packagesListContext */ "./lib/contexts/packagesListContext.js");
/* harmony import */ var _icons_installPackageIcon__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../icons/installPackageIcon */ "./lib/icons/installPackageIcon.js");
/* harmony import */ var _installModal__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./installModal */ "./lib/components/installModal.js");
/* harmony import */ var _installForm__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./installForm */ "./lib/components/installForm.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");






const InstallButton = ({ onStartInstall }) => {
    const { loading } = (0,_contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__.usePackageContext)();
    const [isModalOpen, setIsModalOpen] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const EVENT_NAME = 'mljar-packages-install';
    const [prefillPackage, setPrefillPackage] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(undefined);
    const handleClick = () => {
        setIsModalOpen(true);
    };
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        const onOpen = (e) => {
            var _a;
            const ce = e;
            setPrefillPackage((_a = ce.detail) === null || _a === void 0 ? void 0 : _a.packageName);
            setIsModalOpen(true);
        };
        window.addEventListener(EVENT_NAME, onOpen);
        return () => window.removeEventListener(EVENT_NAME, onOpen);
    }, []);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mljar-packages-manager-install-button", onClick: handleClick, disabled: loading, title: (0,_translator__WEBPACK_IMPORTED_MODULE_2__.t)('Install Packages') },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_icons_installPackageIcon__WEBPACK_IMPORTED_MODULE_3__.installIcon.react, { className: "mljar-packages-manager-install-icon" })),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_installModal__WEBPACK_IMPORTED_MODULE_4__.InstallModal, { isOpen: isModalOpen, onClose: () => setIsModalOpen(false) },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h3", null, (0,_translator__WEBPACK_IMPORTED_MODULE_2__.t)('Install Packages')),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_installForm__WEBPACK_IMPORTED_MODULE_5__.InstallForm, { onClose: () => setIsModalOpen(false), initialPackageName: prefillPackage }))));
};


/***/ }),

/***/ "./lib/components/installForm.js":
/*!***************************************!*\
  !*** ./lib/components/installForm.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   InstallForm: () => (/* binding */ InstallForm)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _contexts_notebookPanelContext__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../contexts/notebookPanelContext */ "./lib/contexts/notebookPanelContext.js");
/* harmony import */ var _pcode_utils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../pcode/utils */ "./lib/pcode/utils.js");
/* harmony import */ var _contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../contexts/packagesListContext */ "./lib/contexts/packagesListContext.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");





const isSuccess = (message) => {
    return ((message === null || message === void 0 ? void 0 : message.toLowerCase().includes((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('success'))) ||
        (message === null || message === void 0 ? void 0 : message.toLowerCase().includes((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('already'))) ||
        false);
};
const InstallForm = ({ onClose, initialPackageName }) => {
    const [packageName, setPackageName] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(initialPackageName !== null && initialPackageName !== void 0 ? initialPackageName : '');
    const [installing, setInstalling] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const [message, setMessage] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(null);
    const [logs, setLogs] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    const interruptedRef = (0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)(false);
    const notebookPanel = (0,_contexts_notebookPanelContext__WEBPACK_IMPORTED_MODULE_2__.useNotebookPanelContext)();
    const { refreshPackages } = (0,_contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_3__.usePackageContext)();
    const logsEndRef = (0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)(null);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        if (initialPackageName !== undefined) {
            setPackageName(initialPackageName);
        }
    }, [initialPackageName]);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        if (logsEndRef.current) {
            logsEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    }, [logs]);
    const appendLog = (text) => {
        const lines = text
            .split(/\r?\n/)
            .filter(line => line.trim() !== '' &&
            !line.includes('NOT_INSTALLED') &&
            !line.includes('INSTALLED') &&
            !line.includes('NOTHING_TO_CHANGE'));
        if (lines.length > 0) {
            setLogs(prev => [...prev, ...lines]);
        }
    };
    const handleStop = () => {
        var _a, _b;
        (_b = (_a = notebookPanel === null || notebookPanel === void 0 ? void 0 : notebookPanel.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel) === null || _b === void 0 ? void 0 : _b.interrupt();
        interruptedRef.current = true;
        setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Installation stopped by user.'));
        setInstalling(false);
    };
    const handleCheckAndInstall = () => {
        var _a, _b;
        setInstalling(true);
        setMessage(null);
        setLogs([]);
        const code = (0,_pcode_utils__WEBPACK_IMPORTED_MODULE_4__.checkIfPackageInstalled)(packageName);
        const future = (_b = (_a = notebookPanel === null || notebookPanel === void 0 ? void 0 : notebookPanel.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel) === null || _b === void 0 ? void 0 : _b.requestExecute({
            code,
            store_history: false
        });
        if (!future) {
            setInstalling(false);
            setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('No kernel available.'));
            return;
        }
        let done = false; // guard to avoid double-handling
        let kickedOffInstall = false;
        const finish = (msgText) => {
            var _a;
            if (done)
                return;
            done = true;
            try {
                (_a = future.dispose) === null || _a === void 0 ? void 0 : _a.call(future);
            }
            catch (_b) {
                /* ignore */
            }
            if (msgText)
                appendLog(msgText);
        };
        // helper: extract printable text from IOPub messages
        const extractText = (msg) => {
            var _a;
            const msgType = msg.header.msg_type;
            // 1) 'stream' -> content.text
            if (msgType === 'stream') {
                const c = msg.content;
                return (_a = c === null || c === void 0 ? void 0 : c.text) !== null && _a !== void 0 ? _a : '';
            }
            // 2) 'execute_result' / 'display_data' / 'update_display_data' -> content.data['text/plain']
            if (msgType === 'execute_result' ||
                msgType === 'display_data' ||
                msgType === 'update_display_data') {
                const c = msg.content;
                const data = (c === null || c === void 0 ? void 0 : c.data) || {};
                // Prefer text/plain. Some envs may return JSON; fall back to JSON stringify.
                if (typeof data['text/plain'] === 'string')
                    return data['text/plain'];
                try {
                    return JSON.stringify(data);
                }
                catch (_b) {
                    return '';
                }
            }
            // Other types not used for user-facing text here
            return '';
        };
        // normalize text for logging/parsing
        const normalize = (s) => (s || '').replace(/\r/g, '\n'); // windows progress uses CR
        future.onIOPub = (msg) => {
            if (done)
                return;
            const msgType = msg.header.msg_type;
            if (msgType === 'stream' ||
                msgType === 'execute_result' ||
                msgType === 'display_data' ||
                msgType === 'update_display_data') {
                const raw = extractText(msg);
                if (!raw)
                    return;
                const text = normalize(raw);
                // Show logs
                appendLog(text);
                // Parse markers from the checker
                if (!kickedOffInstall && text.includes('NOT_INSTALLED')) {
                    kickedOffInstall = true; // guard against multiple triggers
                    proceedWithInstall();
                    // do not finish here; the install flow will setInstalling(false) later
                    return;
                }
                if (text.includes('INSTALLED')) {
                    setInstalling(false);
                    setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Package is already installed.'));
                    finish();
                    return;
                }
                if (text.includes('NOTHING_TO_CHANGE')) {
                    setInstalling(false);
                    setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Requirement already satisfied'));
                    finish();
                    return;
                }
            }
            else if (msgType === 'error') {
                setInstalling(false);
                setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Error while checking installation. Check package name.'));
                finish();
            }
            else if (msgType === 'status') {
                // When kernel says idle after the check and nothing matched, just stop listening.
                const c = msg.content;
                if ((c === null || c === void 0 ? void 0 : c.execution_state) === 'idle' && !kickedOffInstall && !done) {
                    // No recognizable marker came back; end gracefully.
                    setInstalling(false);
                    finish();
                }
            }
        };
        // Also handle the reply channel in case the kernel errors without IOPub error
        future.onReply = (reply) => {
            var _a;
            if (done)
                return;
            const status = (_a = reply.content) === null || _a === void 0 ? void 0 : _a.status;
            if (status === 'error') {
                setInstalling(false);
                setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Error while checking installation. Check package name.'));
                finish();
            }
        };
    };
    const proceedWithInstall = () => {
        var _a, _b;
        const code = (0,_pcode_utils__WEBPACK_IMPORTED_MODULE_4__.installPackagePip)(packageName);
        const future = (_b = (_a = notebookPanel === null || notebookPanel === void 0 ? void 0 : notebookPanel.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel) === null || _b === void 0 ? void 0 : _b.requestExecute({
            code,
            store_history: false
        });
        if (!future) {
            setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('No kernel available.'));
            setInstalling(false);
            return;
        }
        future.onIOPub = (msg) => {
            if (interruptedRef.current) {
                return;
            }
            const msgType = msg.header.msg_type;
            const content = msg.content;
            if (content.text) {
                appendLog(content.text);
            }
            if (msgType === 'error' || content.text.includes('[error]')) {
                setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('An error occurred during installation. Check package name.'));
                setInstalling(false);
            }
            else if (content.text.includes('[done]') ||
                content.text.includes('Successfully installed')) {
                setMessage((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Package installed successfully.'));
                setInstalling(false);
                refreshPackages();
            }
        };
    };
    const resetForm = () => {
        setPackageName('');
        setLogs([]);
        setMessage(null);
        setInstalling(false);
        interruptedRef.current = false;
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-install-form" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-usage-box" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("strong", null,
                (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Usage:'),
                " "),
            " ",
            (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Enter'),
            ' ',
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("code", null, (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('package_name')),
            " ",
            (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('or'),
            ' ',
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("code", null, (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('package_name==version'))),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { type: "text", value: packageName, onChange: e => setPackageName(e.target.value), placeholder: (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Enter package name...'), className: "mljar-packages-manager-install-input", disabled: !!message || installing, onKeyDown: e => {
                if (e.key === 'Enter' && packageName.trim() !== '' && !installing) {
                    handleCheckAndInstall();
                }
            } }),
        logs.length > 0 && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-install-logs" },
            logs.map((line, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { key: idx }, line))),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { ref: logsEndRef }))),
        !message ? (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-install-form-buttons" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mljar-packages-manager-install-submit-button", onClick: handleCheckAndInstall, disabled: installing || packageName.trim() === '' }, installing ? (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-spinner" })) : ((0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Install'))),
            installing && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mljar-packages-manager-stop-button", onClick: handleStop }, "Stop")))) : (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-result" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: `mljar-packages-manager-install-message ${isSuccess(message) ? '' : 'error'}` }, message),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-install-form-buttons" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mljar-packages-manager-install-submit-button", onClick: () => {
                        resetForm();
                    } }, (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Install another package')),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mljar-packages-manager-install-close-button", onClick: onClose }, (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Close')))))));
};


/***/ }),

/***/ "./lib/components/installModal.js":
/*!****************************************!*\
  !*** ./lib/components/installModal.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   InstallModal: () => (/* binding */ InstallModal)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-dom */ "webpack/sharing/consume/default/react-dom");
/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react_dom__WEBPACK_IMPORTED_MODULE_1__);


const InstallModal = ({ isOpen, onClose, children }) => {
    if (!isOpen)
        return null;
    return react_dom__WEBPACK_IMPORTED_MODULE_1___default().createPortal(react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-package-manager-modal-overlay" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-package-manager-content" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mljar-package-manager-modal-close", onClick: onClose }, "\u2716"),
            children)), document.body);
};


/***/ }),

/***/ "./lib/components/packageItem.js":
/*!***************************************!*\
  !*** ./lib/components/packageItem.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   PackageItem: () => (/* binding */ PackageItem)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _icons_deletePackageIcon__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../icons/deletePackageIcon */ "./lib/icons/deletePackageIcon.js");
/* harmony import */ var _pcode_utils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../pcode/utils */ "./lib/pcode/utils.js");
/* harmony import */ var _contexts_notebookPanelContext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../contexts/notebookPanelContext */ "./lib/contexts/notebookPanelContext.js");
/* harmony import */ var _contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../contexts/packagesListContext */ "./lib/contexts/packagesListContext.js");
/* harmony import */ var _icons_errorIcon__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../icons/errorIcon */ "./lib/icons/errorIcon.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");
// src/components/PackageItem.tsx








const PackageItem = ({ pkg }) => {
    const notebookPanel = (0,_contexts_notebookPanelContext__WEBPACK_IMPORTED_MODULE_1__.useNotebookPanelContext)();
    const { refreshPackages } = (0,_contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_2__.usePackageContext)();
    const [loading, setLoading] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const [error, setError] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const handleDelete = async () => {
        var _a, _b;
        let confirmDelete = false;
        if (window.electron) {
            confirmDelete = await window.electron.invoke('show-confirm-dialog', `${(0,_translator__WEBPACK_IMPORTED_MODULE_3__.t)('Click "Ok" to confirm the deletion of')} ${pkg.name}.`);
        }
        else {
            confirmDelete = window.confirm(`${(0,_translator__WEBPACK_IMPORTED_MODULE_3__.t)('Click "Ok" to confirm the deletion of')} ${pkg.name}.`);
        }
        if (!confirmDelete)
            return;
        setLoading(true);
        setError(false);
        const code = (0,_pcode_utils__WEBPACK_IMPORTED_MODULE_4__.removePackagePip)(pkg.name);
        const future = (_b = (_a = notebookPanel === null || notebookPanel === void 0 ? void 0 : notebookPanel.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel) === null || _b === void 0 ? void 0 : _b.requestExecute({
            code,
            store_history: false
        });
        if (!future) {
            setLoading(false);
            setError(true);
            return;
        }
        let done = false;
        const finish = (ok) => {
            var _a;
            if (done)
                return;
            done = true;
            setLoading(false);
            setError(!ok);
            try {
                (_a = future.dispose) === null || _a === void 0 ? void 0 : _a.call(future);
            }
            catch (_b) {
                /* ignore */
            }
        };
        const normalize = (s) => (s || '').replace(/\r/g, '\n');
        const extractText = (msg) => {
            var _a;
            const msgType = msg.header.msg_type;
            if (msgType === 'stream') {
                const c = msg.content;
                return (_a = c === null || c === void 0 ? void 0 : c.text) !== null && _a !== void 0 ? _a : '';
            }
            if (msgType === 'execute_result' ||
                msgType === 'display_data' ||
                msgType === 'update_display_data') {
                const c = msg.content;
                const data = (c === null || c === void 0 ? void 0 : c.data) || {};
                if (typeof data['text/plain'] === 'string')
                    return data['text/plain'];
                try {
                    return JSON.stringify(data);
                }
                catch (_b) {
                    return '';
                }
            }
            return '';
        };
        const handleText = (raw) => {
            if (!raw)
                return;
            const text = normalize(raw);
            // Success markers (our streaming tag or pip's usual line)
            if (text.includes('[done]') ||
                text.includes('Successfully uninstalled')) {
                refreshPackages();
                finish(true);
                return;
            }
            // "Skipping <pkg> as it is not installed." -> treat as success
            if (/\bSkipping\b.*\bas it is not installed\b/i.test(text)) {
                refreshPackages();
                finish(true);
                return;
            }
            // Obvious failures
            if (text.includes('[error]') || /\bERROR\b/.test(text)) {
                finish(false);
                return;
            }
        };
        future.onIOPub = (msg) => {
            if (done)
                return;
            const msgType = msg.header.msg_type;
            if (msgType === 'stream' ||
                msgType === 'execute_result' ||
                msgType === 'display_data' ||
                msgType === 'update_display_data') {
                handleText(extractText(msg));
                return;
            }
            if (msgType === 'error') {
                finish(false);
                return;
            }
            if (msgType === 'status') {
                const c = msg.content;
                if ((c === null || c === void 0 ? void 0 : c.execution_state) === 'idle' && !done) {
                    // If no explicit marker but kernel went idle, assume success and refresh.
                    refreshPackages();
                    finish(true);
                }
            }
        };
        future.onReply = (reply) => {
            var _a;
            if (done)
                return;
            const status = (_a = reply.content) === null || _a === void 0 ? void 0 : _a.status;
            if (status === 'error') {
                finish(false);
            }
        };
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", { className: "mljar-packages-manager-list-item" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "mljar-packages-manager-package-name" },
            " ",
            pkg.name),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "mljar-packages-manager-package-version" }, pkg.version),
        !loading && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mljar-packages-manager-delete-button", onClick: handleDelete, "aria-label": error
                ? `${(0,_translator__WEBPACK_IMPORTED_MODULE_3__.t)('Error during uninstalling')} ${pkg.name}`
                : `${(0,_translator__WEBPACK_IMPORTED_MODULE_3__.t)('Uninstall')} ${pkg.name}`, title: `${(0,_translator__WEBPACK_IMPORTED_MODULE_3__.t)('Delete')} ${pkg.name}` }, error ? (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_icons_errorIcon__WEBPACK_IMPORTED_MODULE_5__.errorIcon.react, { className: "mljar-packages-manager-error-icon" })) : (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_icons_deletePackageIcon__WEBPACK_IMPORTED_MODULE_6__.myDeleteIcon.react, { className: "mljar-packages-manager-delete-icon" })))),
        loading && react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "mljar-packages-manager-spinner" })));
};


/***/ }),

/***/ "./lib/components/packageList.js":
/*!***************************************!*\
  !*** ./lib/components/packageList.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   PackageList: () => (/* binding */ PackageList)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../contexts/packagesListContext */ "./lib/contexts/packagesListContext.js");
/* harmony import */ var _packageItem__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./packageItem */ "./lib/components/packageItem.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");
// src/components/PackageList.tsx




const PackageList = () => {
    const { packages, searchTerm } = (0,_contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__.usePackageContext)();
    const filteredPackages = packages.filter(pkg => pkg.name.toLowerCase().includes(searchTerm.toLowerCase()));
    const listRef = (0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)(null);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        const listEl = listRef.current;
        if (!listEl)
            return;
        const containerEl = listEl.closest('.mljar-packages-manager-list-container') ||
            null;
        if (!containerEl)
            return;
        // function to check if there is overflow
        const checkOverflow = () => {
            const hasOverflowY = listEl.scrollHeight > listEl.clientHeight;
            if (hasOverflowY) {
                listEl.classList.add('package-manager-has-overflow');
                containerEl.classList.add('package-manager-has-overflow');
            }
            else {
                listEl.classList.remove('package-manager-has-overflow');
                containerEl.classList.remove('package-manager-has-overflow');
            }
        };
        checkOverflow();
        window.addEventListener('resize', checkOverflow);
        // hover handle
        const handleMouseEnter = () => {
            const elements = document.querySelectorAll('.package-manager-has-overflow');
            elements.forEach(el => {
                el.style.paddingRight = '5px';
            });
        };
        const handleMouseLeave = () => {
            const elements = document.querySelectorAll('.package-manager-has-overflow');
            elements.forEach(el => {
                el.style.paddingRight = '';
            });
        };
        listEl.addEventListener('mouseenter', handleMouseEnter);
        listEl.addEventListener('mouseleave', handleMouseLeave);
        return () => {
            window.removeEventListener('resize', checkOverflow);
            listEl.removeEventListener('mouseenter', handleMouseEnter);
            listEl.removeEventListener('mouseleave', handleMouseLeave);
        };
    }, [filteredPackages]);
    if (filteredPackages.length === 0) {
        return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", null, (0,_translator__WEBPACK_IMPORTED_MODULE_2__.t)('Sorry, no packages found or notebook is closed.'));
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("ul", { className: "mljar-packages-manager-list", ref: listRef },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", { className: "mljar-packages-manager-list-header" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "mljar-packages-manager-header-name" }, (0,_translator__WEBPACK_IMPORTED_MODULE_2__.t)('Name')),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "mljar-packages-manager-header-version" }, (0,_translator__WEBPACK_IMPORTED_MODULE_2__.t)('Version')),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "mljar-packages-manager-header-blank" }, "\u00A0")),
        filteredPackages
            .sort((a, b) => a.name.localeCompare(b.name))
            .map(pkg => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_packageItem__WEBPACK_IMPORTED_MODULE_3__.PackageItem, { key: pkg.name, pkg: pkg })))));
};


/***/ }),

/***/ "./lib/components/packageListComponent.js":
/*!************************************************!*\
  !*** ./lib/components/packageListComponent.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   PackageListComponent: () => (/* binding */ PackageListComponent)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _components_searchBar__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../components/searchBar */ "./lib/components/searchBar.js");
/* harmony import */ var _components_packageListContent__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../components/packageListContent */ "./lib/components/packageListContent.js");
/* harmony import */ var _components_refreshButton__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../components/refreshButton */ "./lib/components/refreshButton.js");
/* harmony import */ var _components_installButton__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../components/installButton */ "./lib/components/installButton.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");
// src/components/PackageListComponent.tsx






const PackageListComponent = () => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-container" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-header-container" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h3", { className: "mljar-packages-manager-header" }, (0,_translator__WEBPACK_IMPORTED_MODULE_1__.t)('Package Manager')),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_refreshButton__WEBPACK_IMPORTED_MODULE_2__.RefreshButton, null),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_installButton__WEBPACK_IMPORTED_MODULE_3__.InstallButton, { onStartInstall: () => { } })),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_searchBar__WEBPACK_IMPORTED_MODULE_4__.SearchBar, null),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_packageListContent__WEBPACK_IMPORTED_MODULE_5__.PackageListContent, null))));
};


/***/ }),

/***/ "./lib/components/packageListContent.js":
/*!**********************************************!*\
  !*** ./lib/components/packageListContent.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   PackageListContent: () => (/* binding */ PackageListContent)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../contexts/packagesListContext */ "./lib/contexts/packagesListContext.js");
/* harmony import */ var _components_packageList__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../components/packageList */ "./lib/components/packageList.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");




const PackageListContent = () => {
    const { loading, error } = (0,_contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__.usePackageContext)();
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-list-container" },
        loading && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-spinner-container" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-spinner", role: "status", "aria-label": (0,_translator__WEBPACK_IMPORTED_MODULE_2__.t)('Loading...') }))),
        error && react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "mljar-packages-manager-error-message" }, error),
        !loading && !error && react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_packageList__WEBPACK_IMPORTED_MODULE_3__.PackageList, null)));
};


/***/ }),

/***/ "./lib/components/refreshButton.js":
/*!*****************************************!*\
  !*** ./lib/components/refreshButton.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   RefreshButton: () => (/* binding */ RefreshButton)
/* harmony export */ });
/* harmony import */ var _contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../contexts/packagesListContext */ "./lib/contexts/packagesListContext.js");
/* harmony import */ var _icons_refreshIcon__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../icons/refreshIcon */ "./lib/icons/refreshIcon.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");




const RefreshButton = () => {
    const { refreshPackages, loading } = (0,_contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__.usePackageContext)();
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("button", { className: "mljar-packages-manager-refresh-button", onClick: refreshPackages, disabled: loading, title: (0,_translator__WEBPACK_IMPORTED_MODULE_2__.t)('Refresh Packages') },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_icons_refreshIcon__WEBPACK_IMPORTED_MODULE_3__.refreshIcon.react, { className: "mljar-packages-manager-refresh-icon" })));
};


/***/ }),

/***/ "./lib/components/searchBar.js":
/*!*************************************!*\
  !*** ./lib/components/searchBar.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   SearchBar: () => (/* binding */ SearchBar)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../contexts/packagesListContext */ "./lib/contexts/packagesListContext.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");
// src/components/SearchBar.tsx



// import { t } from '../translator';
const SearchBar = () => {
    const { searchTerm, setSearchTerm } = (0,_contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_1__.usePackageContext)();
    const handleChange = (e) => {
        setSearchTerm(e.target.value);
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-search-bar-container" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { type: "text", value: searchTerm, onChange: handleChange, placeholder: (0,_translator__WEBPACK_IMPORTED_MODULE_2__.t)('Search package...'), className: 'mljar-packages-manager-search-bar-input' })));
};


/***/ }),

/***/ "./lib/contexts/notebookKernelContext.js":
/*!***********************************************!*\
  !*** ./lib/contexts/notebookKernelContext.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   NotebookKernelContextProvider: () => (/* binding */ NotebookKernelContextProvider),
/* harmony export */   useNotebookKernelContext: () => (/* binding */ useNotebookKernelContext)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

const NotebookKernelContext = (0,react__WEBPACK_IMPORTED_MODULE_0__.createContext)(null);
function useNotebookKernelContext() {
    return (0,react__WEBPACK_IMPORTED_MODULE_0__.useContext)(NotebookKernelContext);
}
function NotebookKernelContextProvider({ children, notebookWatcher }) {
    const [kernelInfo, setKernelInfo] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(notebookWatcher.kernelInfo);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        const onKernelChanged = (sender, newKernelInfo) => {
            setKernelInfo(newKernelInfo);
        };
        notebookWatcher.kernelChanged.connect(onKernelChanged);
        setKernelInfo(notebookWatcher.kernelInfo);
        return () => {
            notebookWatcher.kernelChanged.disconnect(onKernelChanged);
        };
    }, [notebookWatcher]);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(NotebookKernelContext.Provider, { value: kernelInfo }, children));
}


/***/ }),

/***/ "./lib/contexts/notebookPanelContext.js":
/*!**********************************************!*\
  !*** ./lib/contexts/notebookPanelContext.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   NotebookPanelContextProvider: () => (/* binding */ NotebookPanelContextProvider),
/* harmony export */   useNotebookPanelContext: () => (/* binding */ useNotebookPanelContext)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
// contexts/notebook-panel-context.tsx

const NotebookPanelContext = (0,react__WEBPACK_IMPORTED_MODULE_0__.createContext)(null);
function useNotebookPanelContext() {
    return (0,react__WEBPACK_IMPORTED_MODULE_0__.useContext)(NotebookPanelContext);
}
function NotebookPanelContextProvider({ children, notebookWatcher }) {
    const [notebookPanel, setNotebookPanel] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(notebookWatcher.notebookPanel());
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        const onNotebookPanelChange = (sender, newNotebookPanel) => {
            setNotebookPanel(newNotebookPanel);
        };
        notebookWatcher.notebookPanelChanged.connect(onNotebookPanelChange);
        setNotebookPanel(notebookWatcher.notebookPanel());
        return () => {
            notebookWatcher.notebookPanelChanged.disconnect(onNotebookPanelChange);
        };
    }, [notebookWatcher]);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(NotebookPanelContext.Provider, { value: notebookPanel }, children));
}


/***/ }),

/***/ "./lib/contexts/packagesListContext.js":
/*!*********************************************!*\
  !*** ./lib/contexts/packagesListContext.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CMD_REFRESH_AI_ASSISTANT: () => (/* binding */ CMD_REFRESH_AI_ASSISTANT),
/* harmony export */   CMD_REFRESH_PACKAGES_MANAGER: () => (/* binding */ CMD_REFRESH_PACKAGES_MANAGER),
/* harmony export */   CMD_REFRESH_PIECE_OF_CODE: () => (/* binding */ CMD_REFRESH_PIECE_OF_CODE),
/* harmony export */   PackageContextProvider: () => (/* binding */ PackageContextProvider),
/* harmony export */   STATE_DB_PACKAGES_LIST: () => (/* binding */ STATE_DB_PACKAGES_LIST),
/* harmony export */   STATE_DB_PACKAGES_PANEL_ID: () => (/* binding */ STATE_DB_PACKAGES_PANEL_ID),
/* harmony export */   STATE_DB_PACKAGES_STATUS: () => (/* binding */ STATE_DB_PACKAGES_STATUS),
/* harmony export */   usePackageContext: () => (/* binding */ usePackageContext)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _notebookPanelContext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./notebookPanelContext */ "./lib/contexts/notebookPanelContext.js");
/* harmony import */ var _notebookKernelContext__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./notebookKernelContext */ "./lib/contexts/notebookKernelContext.js");
/* harmony import */ var _pcode_utils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../pcode/utils */ "./lib/pcode/utils.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../translator */ "./lib/translator.js");
// src/contexts/PackageContext.tsx





// constants
// StateDB keys
const STATE_DB_PACKAGES_LIST = 'mljarPackages';
const STATE_DB_PACKAGES_STATUS = 'mljarPackagesStatus';
const STATE_DB_PACKAGES_PANEL_ID = 'mljarPackagesPanelId';
// Commands
const CMD_REFRESH_PIECE_OF_CODE = 'mljar-piece-of-code:refresh-packages'; // force refresh in Piece of Code
const CMD_REFRESH_AI_ASSISTANT = 'mljar-ai-assistant:refresh-packages'; // force refresh in AI Assistant
const CMD_REFRESH_PACKAGES_MANAGER = 'mljar-packages-manager-refresh'; // force refresh in this package
const PackageContext = (0,react__WEBPACK_IMPORTED_MODULE_0__.createContext)(undefined);
let kernelIdToPackagesList = {};
const PackageContextProvider = ({ children, stateDB, commands }) => {
    const notebookPanel = (0,_notebookPanelContext__WEBPACK_IMPORTED_MODULE_1__.useNotebookPanelContext)();
    const kernel = (0,_notebookKernelContext__WEBPACK_IMPORTED_MODULE_2__.useNotebookKernelContext)();
    const [packages, setPackages] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    const [loading, setLoading] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const [error, setError] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(null);
    const [searchTerm, setSearchTerm] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)('');
    const retryCountRef = (0,react__WEBPACK_IMPORTED_MODULE_0__.useRef)(0);
    const setPackagesList = (pkgs) => {
        setPackages(pkgs);
        stateDB.save(STATE_DB_PACKAGES_LIST, JSON.stringify(pkgs));
    };
    const setPackagesStatus = (s) => {
        stateDB.save(STATE_DB_PACKAGES_STATUS, s);
        commands.execute(CMD_REFRESH_PIECE_OF_CODE).catch(err => { });
        commands.execute(CMD_REFRESH_AI_ASSISTANT).catch(err => { });
        if (s === 'loaded' && notebookPanel) {
            stateDB.save(STATE_DB_PACKAGES_PANEL_ID, notebookPanel.id);
        }
        else {
            stateDB.save(STATE_DB_PACKAGES_PANEL_ID, '');
        }
    };
    const executeCode = (0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)(async () => {
        var _a, _b, _c, _d, _e, _f, _g, _h, _j;
        setPackagesList([]);
        setLoading(true);
        setPackagesStatus('loading');
        setError(null);
        if (!notebookPanel || !kernel) {
            setLoading(false);
            setPackagesStatus('unknown');
            return;
        }
        try {
            const kernelId = (_c = (_b = (_a = notebookPanel.sessionContext) === null || _a === void 0 ? void 0 : _a.session) === null || _b === void 0 ? void 0 : _b.kernel) === null || _c === void 0 ? void 0 : _c.id;
            // check if there are packages for current kernel, if yes load them
            // otherwise run code request to Python kernel
            if (kernelId !== undefined &&
                kernelId !== null &&
                kernelId in kernelIdToPackagesList) {
                setPackagesList(kernelIdToPackagesList[kernelId]);
                setLoading(false);
                setPackagesStatus('loaded');
                retryCountRef.current = 0;
            }
            else {
                const future = (_f = (_e = (_d = notebookPanel.sessionContext) === null || _d === void 0 ? void 0 : _d.session) === null || _e === void 0 ? void 0 : _e.kernel) === null || _f === void 0 ? void 0 : _f.requestExecute({
                    code: _pcode_utils__WEBPACK_IMPORTED_MODULE_3__.listPackagesCode,
                    store_history: false
                });
                if (future) {
                    let runAgain = false;
                    future.onIOPub = (msg) => {
                        const msgType = msg.header.msg_type;
                        if (msgType === 'error') {
                            runAgain = true;
                            setLoading(false);
                            setPackagesStatus('error');
                            return;
                        }
                        if (msgType === 'execute_result' ||
                            msgType === 'display_data' ||
                            msgType === 'update_display_data') {
                            const content = msg.content;
                            const jsonData = content.data['application/json'];
                            const textData = content.data['text/plain'];
                            if (jsonData) {
                                if (Array.isArray(jsonData)) {
                                    setPackagesList(jsonData);
                                    setPackagesStatus('loaded');
                                    retryCountRef.current = 0;
                                }
                                else {
                                    console.warn('Data is not JSON:', jsonData);
                                }
                                setLoading(false);
                            }
                            else if (textData) {
                                try {
                                    const cleanedData = textData.replace(/^['"]|['"]$/g, '');
                                    const doubleQuotedData = cleanedData.replace(/'/g, '"');
                                    const parsedData = JSON.parse(doubleQuotedData);
                                    if (Array.isArray(parsedData)) {
                                        setPackagesList([]);
                                        setPackagesList(parsedData);
                                        setPackagesStatus('loaded');
                                        retryCountRef.current = 0;
                                        if (kernelId !== undefined && kernelId !== null) {
                                            kernelIdToPackagesList[kernelId] = parsedData;
                                        }
                                    }
                                    else {
                                        throw new Error('Error during parsing.');
                                    }
                                    setLoading(false);
                                }
                                catch (err) {
                                    console.error('Error during export JSON from text/plain:', err);
                                    setError('Error during export JSON');
                                    setLoading(false);
                                    setPackagesStatus('error');
                                }
                            }
                        }
                    };
                    await future.done;
                    if (runAgain) {
                        // clean JupyterLab displayhook previous cell check
                        (_j = (_h = (_g = notebookPanel.sessionContext) === null || _g === void 0 ? void 0 : _g.session) === null || _h === void 0 ? void 0 : _h.kernel) === null || _j === void 0 ? void 0 : _j.requestExecute({
                            code: 'pass'
                        });
                        if (retryCountRef.current < 1) {
                            retryCountRef.current += 1;
                            setTimeout(executeCode, 100);
                        }
                    }
                }
            }
        }
        catch (err) {
            console.error('Unexpected error:', err);
            setError('Unexpected error');
            setLoading(false);
            setPackagesStatus('error');
        }
    }, [notebookPanel, kernel]);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        if (kernel) {
            executeCode();
        }
    }, [kernel === null || kernel === void 0 ? void 0 : kernel.id]); // run only when kernel.id is changed and kernel is not null
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        commands.addCommand(CMD_REFRESH_PACKAGES_MANAGER, {
            execute: () => {
                kernelIdToPackagesList = {};
                executeCode();
            },
            label: (0,_translator__WEBPACK_IMPORTED_MODULE_4__.t)('Refresh packages in MLJAR Package Manager')
        });
    }, [commands]);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(PackageContext.Provider, { value: {
            packages,
            loading,
            error,
            searchTerm,
            setSearchTerm,
            refreshPackages: () => {
                // clear all stored packages for all kernels
                kernelIdToPackagesList = {};
                executeCode();
            }
        } }, children));
};
const usePackageContext = () => {
    const context = (0,react__WEBPACK_IMPORTED_MODULE_0__.useContext)(PackageContext);
    if (context === undefined) {
        throw new Error('usePackageContext must be used within a PackageProvider');
    }
    return context;
};


/***/ }),

/***/ "./lib/icons/deletePackageIcon.js":
/*!****************************************!*\
  !*** ./lib/icons/deletePackageIcon.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   myDeleteIcon: () => (/* binding */ myDeleteIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);

const svgStr = `
<svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-trash"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 7l16 0" /><path d="M10 11l0 6" /><path d="M14 11l0 6" /><path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" /><path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" /></svg>
`;
const myDeleteIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'my-delete-icon',
    svgstr: svgStr,
});


/***/ }),

/***/ "./lib/icons/errorIcon.js":
/*!********************************!*\
  !*** ./lib/icons/errorIcon.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   errorIcon: () => (/* binding */ errorIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);

const svgStr = `
<svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-zoom-exclamation"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M10 10m-7 0a7 7 0 1 0 14 0a7 7 0 1 0 -14 0" /><path d="M21 21l-6 -6" /><path d="M10 13v.01" /><path d="M10 7v3" /></svg>
`;
const errorIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'my-error-icon',
    svgstr: svgStr,
});


/***/ }),

/***/ "./lib/icons/installPackageIcon.js":
/*!*****************************************!*\
  !*** ./lib/icons/installPackageIcon.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   installIcon: () => (/* binding */ installIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);

const svgStr = `
<svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-cube-plus"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M21 12.5v-4.509a1.98 1.98 0 0 0 -1 -1.717l-7 -4.008a2.016 2.016 0 0 0 -2 0l-7 4.007c-.619 .355 -1 1.01 -1 1.718v8.018c0 .709 .381 1.363 1 1.717l7 4.008a2.016 2.016 0 0 0 2 0" /><path d="M12 22v-10" /><path d="M12 12l8.73 -5.04" /><path d="M3.27 6.96l8.73 5.04" /><path d="M16 19h6" /><path d="M19 16v6" /></svg>
`;
const installIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'my-install-icon',
    svgstr: svgStr,
});


/***/ }),

/***/ "./lib/icons/packageManagerIcon.js":
/*!*****************************************!*\
  !*** ./lib/icons/packageManagerIcon.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   packageManagerIcon: () => (/* binding */ packageManagerIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);

const svgStr = `
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-package-export">
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M12 21l-8 -4.5v-9l8 -4.5l8 4.5v4.5" />
  <path d="M12 12l8 -4.5" />
  <path d="M12 12v9" />
  <path d="M12 12l-8 -4.5" />
  <path d="M15 18h7" />
  <path d="M19 15l3 3l-3 3" />
</svg>
`;
const packageManagerIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'package-manager-icon',
    svgstr: svgStr,
});


/***/ }),

/***/ "./lib/icons/refreshIcon.js":
/*!**********************************!*\
  !*** ./lib/icons/refreshIcon.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   refreshIcon: () => (/* binding */ refreshIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);

const svgStr = `
<svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-refresh"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M20 11a8.1 8.1 0 0 0 -15.5 -2m-.5 -4v4h4" /><path d="M4 13a8.1 8.1 0 0 0 15.5 2m.5 4v-4h-4" /></svg>
`;
const refreshIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'my-refresh-icon',
    svgstr: svgStr
});


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _packageManagerSidebar__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./packageManagerSidebar */ "./lib/packageManagerSidebar.js");
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/statedb */ "webpack/sharing/consume/default/@jupyterlab/statedb");
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./translator */ "./lib/translator.js");
/* harmony import */ var _watchers_notebookWatcher__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./watchers/notebookWatcher */ "./lib/watchers/notebookWatcher.js");





// constants
const PLUGIN_ID = 'mljar-package-manager:plugin';
const COMMAND_INSTALL = 'mljar-package-manager:install';
const EVENT_INSTALL = 'mljar-packages-install';
const TAB_RANK = 1999;
// extension
const leftTab = {
    id: PLUGIN_ID,
    description: 'A JupyterLab extension to list, remove and install python packages from pip.',
    autoStart: true,
    requires: [_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__.IStateDB, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.ITranslator],
    activate: async (app, stateDB, translator) => {
        const lang = translator.languageCode;
        if (lang === 'pl-PL') {
            _translator__WEBPACK_IMPORTED_MODULE_2__.translator.setLanguage('pl');
        }
        const notebookWatcher = new _watchers_notebookWatcher__WEBPACK_IMPORTED_MODULE_3__.NotebookWatcher(app.shell);
        const widget = (0,_packageManagerSidebar__WEBPACK_IMPORTED_MODULE_4__.createPackageManagerSidebar)(notebookWatcher, stateDB, app.commands);
        app.shell.add(widget, 'left', { rank: TAB_RANK });
        // add new command for installing packages
        app.commands.addCommand(COMMAND_INSTALL, {
            label: 'Install Python Package…',
            caption: 'Open MLJAR Package Manager installer',
            execute: args => {
                const pkg = typeof (args === null || args === void 0 ? void 0 : args.package) === 'string' && args.package.trim() !== ''
                    ? args.package.trim()
                    : undefined;
                window.dispatchEvent(new CustomEvent(EVENT_INSTALL, {
                    detail: { packageName: pkg }
                }));
            }
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (leftTab);


/***/ }),

/***/ "./lib/packageManagerSidebar.js":
/*!**************************************!*\
  !*** ./lib/packageManagerSidebar.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   createPackageManagerSidebar: () => (/* binding */ createPackageManagerSidebar)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _icons_packageManagerIcon__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./icons/packageManagerIcon */ "./lib/icons/packageManagerIcon.js");
/* harmony import */ var _contexts_notebookPanelContext__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./contexts/notebookPanelContext */ "./lib/contexts/notebookPanelContext.js");
/* harmony import */ var _contexts_notebookKernelContext__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./contexts/notebookKernelContext */ "./lib/contexts/notebookKernelContext.js");
/* harmony import */ var _components_packageListComponent__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./components/packageListComponent */ "./lib/components/packageListComponent.js");
/* harmony import */ var _contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./contexts/packagesListContext */ "./lib/contexts/packagesListContext.js");
/* harmony import */ var _translator__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./translator */ "./lib/translator.js");








class PackageManagerSidebarWidget extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.ReactWidget {
    constructor(notebookWatcher, stateDB, commands) {
        super();
        this.notebookWatcher = notebookWatcher;
        this.commands = commands;
        this.id = 'package-manager::empty-sidebar';
        this.title.icon = _icons_packageManagerIcon__WEBPACK_IMPORTED_MODULE_2__.packageManagerIcon;
        this.title.caption = (0,_translator__WEBPACK_IMPORTED_MODULE_3__.t)('Package Manager');
        this.addClass('mljar-packages-manager-sidebar-widget');
        this.stateDB = stateDB;
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "mljar-packages-manager-sidebar-container" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_contexts_notebookPanelContext__WEBPACK_IMPORTED_MODULE_4__.NotebookPanelContextProvider, { notebookWatcher: this.notebookWatcher },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_contexts_notebookKernelContext__WEBPACK_IMPORTED_MODULE_5__.NotebookKernelContextProvider, { notebookWatcher: this.notebookWatcher },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_contexts_packagesListContext__WEBPACK_IMPORTED_MODULE_6__.PackageContextProvider, { stateDB: this.stateDB, commands: this.commands },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_packageListComponent__WEBPACK_IMPORTED_MODULE_7__.PackageListComponent, null))))));
    }
}
function createPackageManagerSidebar(notebookWatcher, stateDB, commands) {
    return new PackageManagerSidebarWidget(notebookWatcher, stateDB, commands);
}


/***/ }),

/***/ "./lib/pcode/utils.js":
/*!****************************!*\
  !*** ./lib/pcode/utils.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   checkIfPackageInstalled: () => (/* binding */ checkIfPackageInstalled),
/* harmony export */   installPackagePip: () => (/* binding */ installPackagePip),
/* harmony export */   listPackagesCode: () => (/* binding */ listPackagesCode),
/* harmony export */   removePackagePip: () => (/* binding */ removePackagePip)
/* harmony export */ });
const listPackagesCode = `
def __mljar__list_packages():
    from importlib.metadata import distributions
    pkgs = []
    seen = set()
    for dist in distributions():
        name = dist.metadata["Name"].lower()
        if name not in seen:
            seen.add(name)
            pkgs.append({"name": name, "version": dist.version})
    return pkgs

__mljar__list_packages();
`;
const installPackagePip = (pkg) => `
def __mljar__install_pip(pkg):
    import subprocess, sys

    python_exe = sys.executable
    if python_exe.startswith('\\\\?'):
        python_exe = python_exe[4:]

    cmd = [python_exe, '-m', 'pip', 'install',
           '--progress-bar', 'off', '--no-color',
           '--disable-pip-version-check', *pkg.split()]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

    for line in iter(proc.stdout.readline, ''):
        print(line.replace('\\r', '\\n'), end='')
        sys.stdout.flush()

    proc.stdout.close()
    rc = proc.wait()
    if rc == 0:
        print('[done] Installation OK')
    else:
        print(f'[error] Installation failed:{rc}')

__mljar__install_pip('${pkg}')
`;
const removePackagePip = (pkg) => `
def __mljar__remove_package(pkg):
    import subprocess, sys

    python_exe = sys.executable
    if python_exe.startswith('\\\\?'):
        python_exe = python_exe[4:]

    cmd = [python_exe, '-m', 'pip', 'uninstall', '-y', pkg]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

    for line in iter(proc.stdout.readline, ''):
        print(line.replace('\\r', '\\n'), end='')
        sys.stdout.flush()

    proc.stdout.close()
    rc = proc.wait()
    if rc == 0:
        print('[done] Package removed')
    else:
        print(f'[error] Package removal failed:{rc}')

__mljar__remove_package('${pkg}')
`;
const checkIfPackageInstalled = (pkg) => `
def __mljar__check_if_installed():
    from importlib.metadata import distributions
    from packaging import version
    import re

    m = re.match(r"^([A-Za-z0-9_\\-]+)(==|>=|<=)?([\\w\\.]+)?$", "${pkg}".strip())
    if not m:
        print("INVALID")
        return

    name, op, ver = m.groups()
    name = name.lower()

    for dist in distributions():
        if dist.metadata["Name"].lower() == name:
            if not op:
                print("INSTALLED")
                return

            dist_ver = version.parse(dist.version)
            target_ver = version.parse(ver)

            if op == "==":
                print("NOTHING_TO_CHANGE" if dist_ver == target_ver else "NOT_INSTALLED")
            elif op == ">=":
                print("NOTHING_TO_CHANGE" if dist_ver >= target_ver else "NOT_INSTALLED")
            elif op == "<=":
                print("NOTHING_TO_CHANGE" if dist_ver <= target_ver else "NOT_INSTALLED")
            return

    print("NOT_INSTALLED")

__mljar__check_if_installed()
`;


/***/ }),

/***/ "./lib/translator.js":
/*!***************************!*\
  !*** ./lib/translator.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   t: () => (/* binding */ t),
/* harmony export */   translator: () => (/* binding */ translator)
/* harmony export */ });
class Translator {
    constructor() {
        this.language = 'en';
        this.translations = {
            pl: {
                'Package Manager': 'Menedżer pakietów',
                'Search package...': 'Wyszukaj paczkę...',
                'Install Packages': 'Zainstaluj pakiety',
                'Refresh Packages': 'Odśwież pakiety',
                'Back': 'Wstecz',
                'Go Back': 'Wróć',
                'Loading...': 'Wczytywanie...',
                'Sorry, no packages found or notebook is closed.': 'Nie znaleziono żadnych pakietów lub notatnik nie został otwarty.',
                'Name': 'Nazwa',
                'Version': 'Wersja',
                'Click "Ok" to confirm the deletion of': 'Kliknij "OK", aby potwierdzić usunięcie',
                'Delete': 'Usuń',
                'Uninstall': 'Odinstaluj',
                'Error during uninstalling': 'Błąd podczas instalacji',
                'No kernel available.': 'Brak dostępnego rdzenia obliczeniowego.',
                'Package is already installed.': 'Pakiet jest już zainstalowany.',
                'An error occurred while checking installation. Check the correctness of the package name.': 'Nie udało się zweryfikować instalacji pakietu. Sprawdź, czy nazwa pakietu jest poprawna.',
                'Error installing the package.': 'Błąd podczas instalacji pakietu.',
                'Package installed successfully.': 'Pomyślnie zainstalowano pakiet.',
                'An error occurred during installation. Check the correctness of the package name.': 'Wystąpił błąd podczas instalacji. Sprawdź, czy nazwa pakietu jest poprawna.',
                'Usage:': 'Użycie:',
                'Enter': 'Wpisz',
                'package_name': 'nazwa_pakietu',
                'or': 'lub',
                'package_name==version': 'nazwa_pakietu==wersja',
                'Enter package name...': 'Wpisz nazwę pakietu...',
                'Processing...': 'Przetwarzanie...',
                'Install': 'Zainstaluj',
                'Refresh packages in MLJAR Package Manager': 'Odśwież pakiety w MLJAR Package Manager',
                'success': 'pomyślnie',
                'already': 'już',
                "Installation stopped by user.": "Instalacja zatrzymana przez użytkownika.",
                "Error while checking installation. Check package name.": "Błąd podczas sprawdzania instalacji. Sprawdź nazwę pakietu.",
                "An error occurred during installation. Check package name.": "Wystąpił błąd podczas instalacji. Sprawdź nazwę pakietu.",
                "Install another package": "Zainstaluj kolejny pakiet",
                "Close": "Zamknij",
                "Requirement already satisfied": "Wymagana wersja już jest zainstalowana"
            },
            en: {}
        };
    }
    static getInstance() {
        if (!Translator.instance) {
            Translator.instance = new Translator();
        }
        return Translator.instance;
    }
    setLanguage(lang) {
        this.language = lang;
    }
    translate(text) {
        if (this.language === 'en')
            return text;
        const langTranslations = this.translations[this.language];
        return langTranslations[text] || text;
    }
}
const translator = Translator.getInstance();
const t = (text) => translator.translate(text);


/***/ }),

/***/ "./lib/watchers/notebookWatcher.js":
/*!*****************************************!*\
  !*** ./lib/watchers/notebookWatcher.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   NotebookWatcher: () => (/* binding */ NotebookWatcher)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__);




function getNotebook(widget) {
    if (!(widget instanceof _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__.DocumentWidget)) {
        return null;
    }
    const { content } = widget;
    if (!(content instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.Notebook)) {
        return null;
    }
    return content;
}
class NotebookWatcher {
    constructor(shell) {
        var _a;
        this._kernelInfo = null;
        this._kernelChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this._mainAreaWidget = null;
        this._selections = [];
        this._selectionChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this._notebookPanel = null;
        this._notebookPanelChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this._shell = shell;
        (_a = this._shell.currentChanged) === null || _a === void 0 ? void 0 : _a.connect((sender, args) => {
            this._mainAreaWidget = args.newValue;
            this._notebookPanel = this.notebookPanel();
            this._notebookPanelChanged.emit(this._notebookPanel);
            this._attachKernelChangeHandler();
        });
    }
    get selection() {
        return this._selections;
    }
    get selectionChanged() {
        return this._selectionChanged;
    }
    get notebookPanelChanged() {
        return this._notebookPanelChanged;
    }
    get kernelInfo() {
        return this._kernelInfo;
    }
    get kernelChanged() {
        return this._kernelChanged;
    }
    notebookPanel() {
        const notebook = getNotebook(this._mainAreaWidget);
        if (!notebook) {
            return null;
        }
        return notebook.parent instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.NotebookPanel ? notebook.parent : null;
    }
    _attachKernelChangeHandler() {
        if (this._notebookPanel) {
            const session = this._notebookPanel.sessionContext.session;
            if (session) {
                session.kernelChanged.connect(this._onKernelChanged, this);
                this._updateKernelInfo(session.kernel);
            }
            else {
                setTimeout(() => {
                    var _a;
                    const delayedSession = (_a = this._notebookPanel) === null || _a === void 0 ? void 0 : _a.sessionContext.session;
                    if (delayedSession) {
                        delayedSession.kernelChanged.connect(this._onKernelChanged, this);
                        this._updateKernelInfo(delayedSession.kernel);
                    }
                    else {
                        console.warn('Session not initialized after delay');
                    }
                }, 2000);
            }
        }
        else {
            console.warn('Session not initalizated');
        }
    }
    _onKernelChanged(sender, args) {
        if (args.newValue) {
            this._updateKernelInfo(args.newValue);
        }
        else {
            this._kernelInfo = null;
            this._kernelChanged.emit(null);
        }
    }
    _updateKernelInfo(kernel) {
        this._kernelInfo = {
            name: kernel.name,
            id: kernel.id
        };
        this._kernelChanged.emit(this._kernelInfo);
    }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.04ea5cb2c2f2c8dfb8c7.js.map