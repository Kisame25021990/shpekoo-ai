#!/usr/bin/env python3
"""
Gestion de l'historique des conversations
"""

import json
import os
from datetime import datetime

class ConversationHistory:
    def __init__(self, history_file='history.json'):
        self.history_file = history_file
        self.history = self.load_history()
    
    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"conversations": []}
    
    def save_history(self):
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)
    
    def add_conversation(self, question, answer, source='ai_model'):
        conversation = {
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'answer': answer,
            'source': source
        }
        self.history['conversations'].append(conversation)
        self.save_history()
    
    def get_all(self):
        return self.history['conversations']
    
    def search(self, query):
        results = []
        query_lower = query.lower()
        for conv in self.history['conversations']:
            if query_lower in conv['question'].lower() or query_lower in conv['answer'].lower():
                results.append(conv)
        return results
    
    def get_recent(self, limit=10):
        return self.history['conversations'][-limit:]
    
    def clear(self):
        self.history = {"conversations": []}
        self.save_history()
    
    def stats(self):
        total = len(self.history['conversations'])
        sources = {}
        for conv in self.history['conversations']:
            source = conv.get('source', 'unknown')
            sources[source] = sources.get(source, 0) + 1
        
        return {
            'total_conversations': total,
            'by_source': sources
        }
