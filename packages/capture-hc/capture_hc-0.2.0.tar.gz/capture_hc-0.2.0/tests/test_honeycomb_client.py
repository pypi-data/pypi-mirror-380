import unittest
from unittest.mock import patch, MagicMock
from capture_hc.honeycomb_client import HoneycombClient

class TestHoneycombClient(unittest.TestCase):
    @patch('capture_hc.honeycomb_client.libhoney')
    def test_send_event(self, mock_libhoney):
        client = HoneycombClient('fakekey', 'fakedataset', batch_size=1)  # Force flush after 1 event
        mock_event = MagicMock()
        mock_libhoney.new_event.return_value = mock_event
        fields = {'foo': 'bar', 'baz': 123}
        client.send_event(fields)
        mock_libhoney.new_event.assert_called_once()
        for k, v in fields.items():
            mock_event.add_field.assert_any_call(k, v)
        mock_event.send.assert_called_once()
        mock_libhoney.flush.assert_called_once()

    @patch('capture_hc.honeycomb_client.libhoney')
    def test_timed_decorator(self, mock_libhoney):
        client = HoneycombClient('fakekey', 'fakedataset', batch_size=1)  # Force flush after 1 event
        mock_event = MagicMock()
        mock_libhoney.new_event.return_value = mock_event
        extra_fields = {'alert_name': 'test_func'}
        @client.timed(extra_fields)
        def dummy(event=None):
            event.add_field('custom', 42)
            return 'done'
        result = dummy()
        self.assertEqual(result, 'done')
        mock_libhoney.new_event.assert_called_once()
        mock_event.add_field.assert_any_call('alert_name', 'test_func')
        mock_event.add_field.assert_any_call('custom', 42)
        mock_event.add_field.assert_any_call('duration_ms', unittest.mock.ANY)
        mock_event.add_field.assert_any_call('function_name', 'dummy')
        mock_event.send.assert_called_once()
        mock_libhoney.flush.assert_called_once()

    @patch('capture_hc.honeycomb_client.libhoney')
    def test_instance_run_with_timing(self, mock_libhoney):
        from capture_hc import HoneycombClient
        client = HoneycombClient('k', 'd', batch_size=1)  # Force flush after 1 event
        mock_event = MagicMock()
        mock_libhoney.new_event.return_value = mock_event

        def sample(a, b, event=None):
            event.add_field('sum', a + b)
            return a + b

        result = client.run_with_timing(sample, 4, 6, extra_fields={'alert_name': 'sample'})
        self.assertEqual(result, 10)
        mock_libhoney.new_event.assert_called()
        mock_event.add_field.assert_any_call('alert_name', 'sample')
        mock_event.add_field.assert_any_call('sum', 10)
        mock_event.add_field.assert_any_call('duration_ms', unittest.mock.ANY)
        mock_event.add_field.assert_any_call('function_name', 'sample')
        mock_event.send.assert_called_once()
        mock_libhoney.flush.assert_called()

    @patch('capture_hc.honeycomb_client.libhoney')
    def test_class_call_with_timing(self, mock_libhoney):
        from capture_hc import HoneycombClient
        mock_event = MagicMock()
        mock_libhoney.new_event.return_value = mock_event

        def sample(a, b, event=None):
            event.add_field('sum', a + b)
            return a + b

        result = HoneycombClient.call_with_timing(
            sample,
            7,
            8,
            writekey='k',
            dataset='d',
            extra_fields={'alert_name': 'sample'},
            batch_size=1,  # Force flush after 1 event
        )
        self.assertEqual(result, 15)
        mock_libhoney.new_event.assert_called()
        mock_event.add_field.assert_any_call('alert_name', 'sample')
        mock_event.add_field.assert_any_call('sum', 15)
        mock_event.add_field.assert_any_call('duration_ms', unittest.mock.ANY)
        mock_event.add_field.assert_any_call('function_name', 'sample')
        mock_event.send.assert_called_once()
        mock_libhoney.flush.assert_called()

    @patch('capture_hc.honeycomb_client.libhoney')
    def test_lazy_timed_env_no_injection(self, mock_libhoney):
        from capture_hc import HoneycombClient
        from unittest.mock import patch as mock_patch

        with mock_patch.dict('os.environ', {
            'HONEYCOMB_WRITEKEY': 'kw',
            'HONEYCOMB_DATASET': 'ds'
        }, clear=False):
            mock_event = MagicMock()
            mock_libhoney.new_event.return_value = mock_event

            @HoneycombClient.lazy_timed(extra_fields={'alert_name': 'legacy_task'}, event_arg=None)
            def legacy_task(x, y):
                return x + y

            result = legacy_task(2, 3)
            self.assertEqual(result, 5)
            mock_libhoney.init.assert_called_with(
                writekey='kw', 
                dataset='ds', 
                debug=False,
                max_concurrent_batches=10,
                block_on_send=False,
                block_on_response=False
            )
            mock_event.add_field.assert_any_call('alert_name', 'legacy_task')
            mock_event.add_field.assert_any_call('duration_ms', unittest.mock.ANY)
            mock_event.add_field.assert_any_call('function_name', 'legacy_task')
            mock_event.send.assert_called_once()
            mock_libhoney.flush.assert_called_once()

    @patch('capture_hc.honeycomb_client.libhoney')
    def test_lazy_timed_env_with_injection(self, mock_libhoney):
        from capture_hc import HoneycombClient
        from unittest.mock import patch as mock_patch

        with mock_patch.dict('os.environ', {
            'HONEYCOMB_WRITEKEY': 'kw',
            'HONEYCOMB_DATASET': 'ds'
        }, clear=False):
            mock_event = MagicMock()
            mock_libhoney.new_event.return_value = mock_event

            @HoneycombClient.lazy_timed(extra_fields={'alert_name': 'with_event'})
            def fn(a, b, event=None):
                event.add_field('sum', a + b)
                return a + b

            out = fn(4, 6)
            self.assertEqual(out, 10)
            mock_event.add_field.assert_any_call('alert_name', 'with_event')
            mock_event.add_field.assert_any_call('sum', 10)
            mock_event.add_field.assert_any_call('duration_ms', unittest.mock.ANY)
            mock_event.add_field.assert_any_call('function_name', 'fn')
            mock_event.send.assert_called_once()
            mock_libhoney.flush.assert_called_once()

    def test_lazy_timed_missing_creds_raises(self):
        from capture_hc import HoneycombClient
        from unittest.mock import patch as mock_patch

        with mock_patch.dict('os.environ', {}, clear=True):
            with self.assertRaises(ValueError):
                @HoneycombClient.lazy_timed(extra_fields={'alert_name': 'x'})
                def fn(a, b):
                    return a + b
                fn(1, 2)

    @patch('capture_hc.honeycomb_client.libhoney')
    def test_connection_management_batching(self, mock_libhoney):
        """Test that events are batched and flushed appropriately."""
        client = HoneycombClient('fakekey', 'fakedataset', batch_size=3, flush_interval=10.0)
        mock_event = MagicMock()
        mock_libhoney.new_event.return_value = mock_event
        
        # Send 2 events (should not flush yet)
        client.send_event({'event': 1})
        client.send_event({'event': 2})
        self.assertEqual(mock_libhoney.flush.call_count, 0)
        
        # Send 3rd event (should trigger flush)
        client.send_event({'event': 3})
        self.assertEqual(mock_libhoney.flush.call_count, 1)
        
        # Send 2 more events (should not flush yet)
        client.send_event({'event': 4})
        client.send_event({'event': 5})
        self.assertEqual(mock_libhoney.flush.call_count, 1)
        
        # Force flush
        client.flush()
        self.assertEqual(mock_libhoney.flush.call_count, 2)

    @patch('capture_hc.honeycomb_client.libhoney')
    def test_close_method(self, mock_libhoney):
        """Test that close method flushes remaining events."""
        client = HoneycombClient('fakekey', 'fakedataset', batch_size=10)
        mock_event = MagicMock()
        mock_libhoney.new_event.return_value = mock_event
        
        # Send some events
        client.send_event({'event': 1})
        client.send_event({'event': 2})
        
        # Close should flush remaining events
        client.close()
        mock_libhoney.flush.assert_called()

if __name__ == '__main__':
    unittest.main() 