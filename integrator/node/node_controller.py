

self._load_system_details()
        if self._hash_exists():
            self._logger.debug(_('Found an existing node and same will be booted'))
        else:
            self._logger.info(_('No previous intallation found on this node'))
            response = confirm(message=_('A new node will be configured. Proceed(Y/N): '))

            if response:
                self._create_node()
            else:
                self._logger.info(_('Configuration terminated as per the selection'))
