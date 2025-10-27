from subject_api import SubjectAPI

DB_CONNECTION_STRING = "postgresql://postgres:0301@localhost:5432/QA"


class TestSubjects:
    def setup_method(self):
        self.subject_api = SubjectAPI(DB_CONNECTION_STRING)

    def teardown_method(self):
        test_ids = [100, 101, 150]
        for test_id in test_ids:
            self.subject_api.cleanup_subject(test_id)

    def test_select_subject(self):
        rows = self.subject_api.select_subject_by_id(1)

        assert len(rows) == 1
        assert rows[0]["subject_title"] == "English"

    def test_add_subject(self):
        test_subject_id = 100
        test_subject_title = "Испанский язык"

        self.subject_api.cleanup_subject(test_subject_id)

        success = self.subject_api.add_subject(test_subject_id, test_subject_title)

        assert success, "Предмет не был добавлен в таблицу"

        rows = self.subject_api.select_subject_by_id(test_subject_id)
        assert len(rows) == 1
        assert rows[0]["subject_id"] == test_subject_id
        assert rows[0]["subject_title"] == test_subject_title


    def test_update_subject(self):
        test_subject_id = 101
        old_title = "Немецкий язык"
        new_title = "Голландский язык"

        self.subject_api.cleanup_subject(test_subject_id)

        self.subject_api.add_subject(test_subject_id, old_title)

        row_count = self.subject_api.update_subject(test_subject_id, new_title)

        assert row_count == 1, "Предмет не был изменен"

        rows = self.subject_api.select_subject_by_id(test_subject_id)
        assert len(rows) == 1
        assert rows[0]["subject_title"] == new_title


    def test_delete_subject(self):
        test_subject_id = 150
        test_subject_title = "Французский язык"

        self.subject_api.cleanup_subject(test_subject_id)

        self.subject_api.add_subject(test_subject_id, test_subject_title)

        count_before = self.subject_api.get_subject_count(test_subject_id)
        assert count_before == 1, "Предмет не был добавлен перед удалением"

        delete_count = self.subject_api.delete_subject(test_subject_id)

        assert delete_count == 1, "Предмет не был удален"

        count_after = self.subject_api.get_subject_count(test_subject_id)
        assert count_after == 0, "Предмет все еще существует после удаления"
