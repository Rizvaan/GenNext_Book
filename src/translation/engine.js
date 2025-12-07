/**
 * Translation Engine for AI-Native Textbook
 * Handles translation between English and Urdu
 */

class TranslationEngine {
    constructor() {
        // In a real implementation, this would connect to a translation API
        // For this example, we'll use a simple mock translation approach
        this.translationCache = new Map();
        this.supportedLanguages = ['en', 'ur'];
    }

    /**
     * Translate content from source language to target language
     * @param {string} content - Content to translate
     * @param {string} sourceLang - Source language code (e.g. 'en')
     * @param {string} targetLang - Target language code (e.g. 'ur')
     * @returns {string} - Translated content
     */
    async translate(content, sourceLang = 'en', targetLang = 'ur') {
        // Check if translation is already cached
        const cacheKey = `${sourceLang}-${targetLang}:${content.substring(0, 50)}`;
        if (this.translationCache.has(cacheKey)) {
            return this.translationCache.get(cacheKey);
        }

        // Validate language support
        if (!this.supportedLanguages.includes(sourceLang) || !this.supportedLanguages.includes(targetLang)) {
            throw new Error(`Unsupported language pair: ${sourceLang} -> ${targetLang}`);
        }

        // In a real implementation, this would call an actual translation API
        // For demo purposes, we'll return the original content with a note
        let translatedContent;
        
        if (sourceLang === 'en' && targetLang === 'ur') {
            // Mock translation from English to Urdu
            translatedContent = await this.translateEnglishToUrdu(content);
        } else if (sourceLang === 'ur' && targetLang === 'en') {
            // Mock translation from Urdu to English
            translatedContent = await this.translateUrduToEnglish(content);
        } else {
            // If source and target are the same or not supported
            translatedContent = content;
        }

        // Cache the translation
        this.translationCache.set(cacheKey, translatedContent);

        return translatedContent;
    }

    /**
     * Translate English to Urdu
     * @param {string} content - English content to translate
     * @returns {string} - Urdu translation
     */
    async translateEnglishToUrdu(content) {
        // This is a mock implementation that would in reality call a translation API
        // In a real implementation, you would use something like Google Translate API
        return ` mock_urdu_translation(${content}) `;
    }

    /**
     * Translate Urdu to English
     * @param {string} content - Urdu content to translate
     * @returns {string} - English translation
     */
    async translateUrduToEnglish(content) {
        // This is a mock implementation that would in reality call a translation API
        return `mock_en_translation(${content})`;
    }

    /**
     * Translate specific technical terms
     * @param {string} term - Technical term to translate
     * @returns {string} - Translated term
     */
    translateTechnicalTerm(term, targetLang) {
        // Define technical term mappings
        const technicalTerms = {
            'robotics': {
                'ur': 'روبوٹکس',
            },
            'AI': {
                'ur': 'مصنوعی ذہانت',
            },
            'ROS': {
                'ur': 'روبوٹ آپریٹنگ سسٹم',
            },
            'Node': {
                'ur': 'نود',
            },
            'Topic': {
                'ur': 'ٹاپک',
            },
            'Service': {
                'ur': 'سروس',
            },
            'humanoid': {
                'ur': 'انسان نما',
            },
            'simulation': {
                'ur': 'تقلید',
            },
            'SLAM': {
                'ur': 'ایس ایل اے ایم',
            },
            'navigation': {
                'ur': 'رہ نما',
            },
            'path planning': {
                'ur': 'راستہ منصوبہ بندی',
            }
        };

        if (technicalTerms[term] && technicalTerms[term][targetLang]) {
            return technicalTerms[term][targetLang];
        }
        
        // If no specific translation exists, return the original term
        return term;
    }

    /**
     * Get supported languages
     * @returns {array} - List of supported language codes
     */
    getSupportedLanguages() {
        return [...this.supportedLanguages];
    }

    /**
     * Pre-translate content to improve performance
     * @param {string} content - Content to pre-translate
     * @param {string} sourceLang - Source language
     * @param {string} targetLang - Target language
     */
    async preTranslate(content, sourceLang, targetLang) {
        // In a real implementation, this would do batch translation
        // to improve performance when content is requested
        return this.translate(content, sourceLang, targetLang);
    }
}

// Export the engine
export default TranslationEngine;