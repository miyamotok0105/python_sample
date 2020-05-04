#!/usr/bin/env python
# -*- coding: utf-8 -*-

class IssueFactory():
    def create(self, question, answer):
        template = "### Question\n{0}\n\n### Answer\n{1}".format(question, answer)
        return template

if __name__ == '__main__':
    issue_factory = IssueFactory()
    print(issue_factory.create("質問", "回答"))
    
    print(issue_factory.create("質問\n2行目", "回答"))
