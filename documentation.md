# Hazelcast Open Binary Client Protocol

**Revision History**

| Date | Document Version | Change Description |
| ---- | ---------------- | ------------------ |
| 01/15/2020 | 2.0 | Release of the Hazelcast Open Binary Client Protocol version 2.0 |
| 11/04/2020 | 2.1 | Release of the Hazelcast Open Binary Client Protocol version 2.1 |

**Table of Contents**
- [1. Introduction](#1-introduction)
- [2. Data Format Details](#2-data-format-details)
    - [2.1. Client Message](#21-client-message)
        - [2.1.1. Frame](#211-frame)
        - [2.1.2. Initial Frame](#212-initial-frame)
            - [2.1.2.1. Message Type](#2121-message-type)
                - [2.1.2.1.1. Request Message Type](#21211-request-message-type)
                - [2.1.2.1.2. Response Message Type](#21212-response-message-type)
                - [2.1.2.1.3. Event Response Message Type](#21213-event-response-message-type)
                - [2.1.2.1.4. Error Message Type](#21214-error-message-type)
            - [2.1.2.2. Correlation ID](#2122-correlation-id)
            - [2.1.2.3. Partition ID](#2123-partition-id)
            - [2.1.2.4. Backup Acks Count](#2124-backup-acks-count)
        - [2.1.3. Encoding of Variable Sized Parameters](#213-encoding-of-variable-sized-parameters)
            - [2.1.3.1. Encoding of String Parameters](#2131-encoding-of-string-parameters)
            - [2.1.3.2. Encoding of Custom Type Parameters](#2132-encoding-of-custom-type-parameters)
            - [2.1.3.3. Encoding of List Parameters](#2133-encoding-of-list-parameters)
                - [2.1.3.3.1. Encoding of List of Fix Sized Parameters](#21331-encoding-of-list-of-fix-sized-parameters)
                - [2.1.3.3.2. Encoding of List of Variable Sized Parameters](#21332-encoding-of-list-of-variable-sized-parameters)
            - [2.1.3.4. Encoding of Map Parameters](#21333-encoding-of-map-parameters)
        - [2.1.4. Client Message Fragmentation](#214-client-message-fragmentation)
        - [2.1.5. Client Message Boundaries](#215-client-message-boundaries)
        - [2.1.6. Backward Compatibility of the Client Messages](#216-backward-compatibility-of-the-client-messages)
        - [2.1.7. Augmented Backus-Naur Format Representation of the Client Messages](#217-augmented-backusnaur-format-representation-of-the-client-messages)
    - [3. Client Protocol Data Types](#3-client-protocol-data-types)
    - [4. Connection Guide](#4-connection-guide)
        - [4.1. Opening a Connection](#41-opening-a-connection)
        - [4.2. Connection Initialization](#42-connection-initialization)
        - [4.3. Authentication](#43-authentication)
        - [4.4. Communication](#44-communication)
        - [4.5. Closing Connections](#45-closing-connections)
    - [5. Requests and Responses](#5-requests-and-responses)
        - [5.1. Distributed Objects](#51-distributed-objects)
        - [5.2. Operation Messages and Responses](#52-operation-messages-and-responses)
        - [5.3. Proxies](#53-proxies)
            - [5.3.1. Proxy Creation](#531-proxy-creation)
            - [5.3.2. List Example](#532-list-example)
            - [5.3.3. Fenced Lock Example](#533-fenced-lock-example)
            - [5.3.4. Map Example](#534-map-example)
            - [5.3.5. Queue Example](#535-queue-example)
            - [5.3.6. Set Example](#536-set-example)
        - [5.4. Multiple Responses to a Single Request](#54-multiple-responses-to-a-single-request)
        - [5.5. Listeners](#55-listeners)
        - [5.6. Cluster View Listener](#56-cluster-view-listener)
        - [5.7. Timeouts and Retry](#57-timeouts-and-retry)
        - [5.8. Error Codes](#58-error-codes)
    - [6. Miscellaneous](#6-miscellaneous)
        - [6.1. Smart Client and Unisocket Client](#61-smart-client-and-unisocket-client)
        - [6.2. Serialization](#62-serialization)
        - [6.3. Security](#63-security)
    - [7. Protocol Messages](#7-protocol-messages)
        - [7.1. Custom Data Types Used In The Protocol](#71-custom-data-types-used-in-the-protocol)
            - [7.1.1. Address](#711-address)
            - [7.1.2. CacheEventData](#712-cacheeventdata)
            - [7.1.3. CacheSimpleEntryListenerConfig](#713-cachesimpleentrylistenerconfig)
            - [7.1.4. DistributedObjectInfo](#714-distributedobjectinfo)
            - [7.1.5. ErrorHolder](#715-errorholder)
            - [7.1.6. EventJournalConfig](#716-eventjournalconfig)
            - [7.1.7. EvictionConfigHolder](#717-evictionconfigholder)
            - [7.1.8. HotRestartConfig](#718-hotrestartconfig)
            - [7.1.9. ListenerConfigHolder](#719-listenerconfigholder)
            - [7.1.10. AttributeConfig](#7110-attributeconfig)
            - [7.1.11. IndexConfig](#7111-indexconfig)
            - [7.1.12. BitmapIndexOptions](#7112-bitmapindexoptions)
            - [7.1.13. BTreeIndexConfig](#7113-btreeindexconfig)
            - [7.1.14. MapStoreConfigHolder](#7114-mapstoreconfigholder)
            - [7.1.15. MerkleTreeConfig](#7115-merkletreeconfig)
            - [7.1.16. NearCacheConfigHolder](#7116-nearcacheconfigholder)
            - [7.1.17. NearCachePreloaderConfig](#7117-nearcachepreloaderconfig)
            - [7.1.18. PredicateConfigHolder](#7118-predicateconfigholder)
            - [7.1.19. QueryCacheConfigHolder](#7119-querycacheconfigholder)
            - [7.1.20. QueryCacheEventData](#7120-querycacheeventdata)
            - [7.1.21. QueueStoreConfigHolder](#7121-queuestoreconfigholder)
            - [7.1.22. RaftGroupId](#7122-raftgroupid)
            - [7.1.23. RingbufferStoreConfigHolder](#7123-ringbufferstoreconfigholder)
            - [7.1.24. ScheduledTaskHandler](#7124-scheduledtaskhandler)
            - [7.1.25. SimpleEntryView](#7125-simpleentryview)
            - [7.1.26. StackTraceElement](#7126-stacktraceelement)
            - [7.1.27. DurationConfig](#7127-durationconfig)
            - [7.1.28. TimedExpiryPolicyFactoryConfig](#7128-timedexpirypolicyfactoryconfig)
            - [7.1.29. WanReplicationRef](#7129-wanreplicationref)
            - [7.1.30. Xid](#7130-xid)
            - [7.1.31. MergePolicyConfig](#7131-mergepolicyconfig)
            - [7.1.32. CacheConfigHolder](#7132-cacheconfigholder)
            - [7.1.33. ClientBwListEntry](#7133-clientbwlistentry)
            - [7.1.34. MemberInfo](#7134-memberinfo)
            - [7.1.35. EndpointQualifier](#7135-endpointqualifier)
            - [7.1.36. MemberVersion](#7136-memberversion)
            - [7.1.37. MCEvent](#7137-mcevent)
            - [7.1.38. AnchorDataListHolder](#7138-anchordatalistholder)
            - [7.1.39. PagingPredicateHolder](#7139-pagingpredicateholder)
            - [7.1.40. SqlQueryId](#7140-sqlqueryid)
            - [7.1.41. SqlError](#7141-sqlerror)
            - [7.1.42. SqlColumnMetadata](#7142-sqlcolumnmetadata)
            - [7.1.43. CPMember](#7143-cpmember)
            - [7.1.44. MigrationState](#7144-migrationstate)
            - [7.1.45. FieldDescriptor](#7145-fielddescriptor)
            - [7.1.46. Schema](#7146-schema)
            - [7.1.47. HazelcastJsonValue](#7147-hazelcastjsonvalue)
            - [7.1.48. DataPersistenceConfig](#7148-datapersistenceconfig)
            - [7.1.49. Capacity](#7149-capacity)
            - [7.1.50. MemoryTierConfig](#7150-memorytierconfig)
            - [7.1.51. DiskTierConfig](#7151-disktierconfig)
            - [7.1.52. TieredStoreConfig](#7152-tieredstoreconfig)
            - [7.1.53. SqlSummary](#7153-sqlsummary)
            - [7.1.54. JobAndSqlSummary](#7154-jobandsqlsummary)
            - [7.1.55. PartitioningAttributeConfig](#7155-partitioningattributeconfig)
            - [7.1.56. WanConsumerConfigHolder](#7156-wanconsumerconfigholder)
            - [7.1.57. WanCustomPublisherConfigHolder](#7157-wancustompublisherconfigholder)
            - [7.1.58. WanBatchPublisherConfigHolder](#7158-wanbatchpublisherconfigholder)
            - [7.1.59. AwsConfig](#7159-awsconfig)
            - [7.1.60. GcpConfig](#7160-gcpconfig)
            - [7.1.61. AzureConfig](#7161-azureconfig)
            - [7.1.62. KubernetesConfig](#7162-kubernetesconfig)
            - [7.1.63. EurekaConfig](#7163-eurekaconfig)
            - [7.1.64. DiscoveryStrategyConfig](#7164-discoverystrategyconfig)
            - [7.1.65. DiscoveryConfig](#7165-discoveryconfig)
            - [7.1.66. WanSyncConfig](#7166-wansyncconfig)
            - [7.1.67. ReplicatedMapEntryViewHolder](#7167-replicatedmapentryviewholder)
            - [7.1.68. ResourceDefinition](#7168-resourcedefinition)
            - [7.1.69. VectorIndexConfig](#7169-vectorindexconfig)
            - [7.1.70. VectorPair](#7170-vectorpair)
            - [7.1.71. VectorDocument](#7171-vectordocument)
            - [7.1.72. VectorSearchOptions](#7172-vectorsearchoptions)
            - [7.1.73. VectorSearchResult](#7173-vectorsearchresult)
            - [7.1.74. Version](#7174-version)
            - [7.1.75. RaftGroupInfo](#7175-raftgroupinfo)
        - [7.2. Client](#72-client)
            - [7.2.1. Client.Authentication](#721-clientauthentication)
            - [7.2.2. Client.AuthenticationCustom](#722-clientauthenticationcustom)
            - [7.2.3. Client.AddClusterViewListener](#723-clientaddclusterviewlistener)
            - [7.2.4. Client.CreateProxy](#724-clientcreateproxy)
            - [7.2.5. Client.DestroyProxy](#725-clientdestroyproxy)
            - [7.2.6. Client.AddPartitionLostListener](#726-clientaddpartitionlostlistener)
            - [7.2.7. Client.RemovePartitionLostListener](#727-clientremovepartitionlostlistener)
            - [7.2.8. Client.GetDistributedObjects](#728-clientgetdistributedobjects)
            - [7.2.9. Client.AddDistributedObjectListener](#729-clientadddistributedobjectlistener)
            - [7.2.10. Client.RemoveDistributedObjectListener](#7210-clientremovedistributedobjectlistener)
            - [7.2.11. Client.Ping](#7211-clientping)
            - [7.2.12. Client.Statistics](#7212-clientstatistics)
            - [7.2.13. Client.DeployClasses](#7213-clientdeployclasses)
            - [7.2.14. Client.CreateProxies](#7214-clientcreateproxies)
            - [7.2.15. Client.LocalBackupListener](#7215-clientlocalbackuplistener)
            - [7.2.16. Client.TriggerPartitionAssignment](#7216-clienttriggerpartitionassignment)
            - [7.2.17. Client.AddMigrationListener](#7217-clientaddmigrationlistener)
            - [7.2.18. Client.RemoveMigrationListener](#7218-clientremovemigrationlistener)
            - [7.2.19. Client.SendSchema](#7219-clientsendschema)
            - [7.2.20. Client.FetchSchema](#7220-clientfetchschema)
            - [7.2.21. Client.SendAllSchemas](#7221-clientsendallschemas)
            - [7.2.22. Client.TpcAuthentication](#7222-clienttpcauthentication)
            - [7.2.23. Client.AddCPGroupViewListener](#7223-clientaddcpgroupviewlistener)
        - [7.3. Map](#73-map)
            - [7.3.1. Map.Put](#731-mapput)
            - [7.3.2. Map.Get](#732-mapget)
            - [7.3.3. Map.Remove](#733-mapremove)
            - [7.3.4. Map.Replace](#734-mapreplace)
            - [7.3.5. Map.ReplaceIfSame](#735-mapreplaceifsame)
            - [7.3.6. Map.ContainsKey](#736-mapcontainskey)
            - [7.3.7. Map.ContainsValue](#737-mapcontainsvalue)
            - [7.3.8. Map.RemoveIfSame](#738-mapremoveifsame)
            - [7.3.9. Map.Delete](#739-mapdelete)
            - [7.3.10. Map.Flush](#7310-mapflush)
            - [7.3.11. Map.TryRemove](#7311-maptryremove)
            - [7.3.12. Map.TryPut](#7312-maptryput)
            - [7.3.13. Map.PutTransient](#7313-mapputtransient)
            - [7.3.14. Map.PutIfAbsent](#7314-mapputifabsent)
            - [7.3.15. Map.Set](#7315-mapset)
            - [7.3.16. Map.Lock](#7316-maplock)
            - [7.3.17. Map.TryLock](#7317-maptrylock)
            - [7.3.18. Map.IsLocked](#7318-mapislocked)
            - [7.3.19. Map.Unlock](#7319-mapunlock)
            - [7.3.20. Map.AddInterceptor](#7320-mapaddinterceptor)
            - [7.3.21. Map.RemoveInterceptor](#7321-mapremoveinterceptor)
            - [7.3.22. Map.AddEntryListenerToKeyWithPredicate](#7322-mapaddentrylistenertokeywithpredicate)
            - [7.3.23. Map.AddEntryListenerWithPredicate](#7323-mapaddentrylistenerwithpredicate)
            - [7.3.24. Map.AddEntryListenerToKey](#7324-mapaddentrylistenertokey)
            - [7.3.25. Map.AddEntryListener](#7325-mapaddentrylistener)
            - [7.3.26. Map.RemoveEntryListener](#7326-mapremoveentrylistener)
            - [7.3.27. Map.AddPartitionLostListener](#7327-mapaddpartitionlostlistener)
            - [7.3.28. Map.RemovePartitionLostListener](#7328-mapremovepartitionlostlistener)
            - [7.3.29. Map.GetEntryView](#7329-mapgetentryview)
            - [7.3.30. Map.Evict](#7330-mapevict)
            - [7.3.31. Map.EvictAll](#7331-mapevictall)
            - [7.3.32. Map.LoadAll](#7332-maploadall)
            - [7.3.33. Map.LoadGivenKeys](#7333-maploadgivenkeys)
            - [7.3.34. Map.KeySet](#7334-mapkeyset)
            - [7.3.35. Map.GetAll](#7335-mapgetall)
            - [7.3.36. Map.Values](#7336-mapvalues)
            - [7.3.37. Map.EntrySet](#7337-mapentryset)
            - [7.3.38. Map.KeySetWithPredicate](#7338-mapkeysetwithpredicate)
            - [7.3.39. Map.ValuesWithPredicate](#7339-mapvalueswithpredicate)
            - [7.3.40. Map.EntriesWithPredicate](#7340-mapentrieswithpredicate)
            - [7.3.41. Map.AddIndex](#7341-mapaddindex)
            - [7.3.42. Map.Size](#7342-mapsize)
            - [7.3.43. Map.IsEmpty](#7343-mapisempty)
            - [7.3.44. Map.PutAll](#7344-mapputall)
            - [7.3.45. Map.Clear](#7345-mapclear)
            - [7.3.46. Map.ExecuteOnKey](#7346-mapexecuteonkey)
            - [7.3.47. Map.SubmitToKey](#7347-mapsubmittokey)
            - [7.3.48. Map.ExecuteOnAllKeys](#7348-mapexecuteonallkeys)
            - [7.3.49. Map.ExecuteWithPredicate](#7349-mapexecutewithpredicate)
            - [7.3.50. Map.ExecuteOnKeys](#7350-mapexecuteonkeys)
            - [7.3.51. Map.ForceUnlock](#7351-mapforceunlock)
            - [7.3.52. Map.KeySetWithPagingPredicate](#7352-mapkeysetwithpagingpredicate)
            - [7.3.53. Map.ValuesWithPagingPredicate](#7353-mapvalueswithpagingpredicate)
            - [7.3.54. Map.EntriesWithPagingPredicate](#7354-mapentrieswithpagingpredicate)
            - [7.3.55. Map.FetchKeys](#7355-mapfetchkeys)
            - [7.3.56. Map.FetchEntries](#7356-mapfetchentries)
            - [7.3.57. Map.Aggregate](#7357-mapaggregate)
            - [7.3.58. Map.AggregateWithPredicate](#7358-mapaggregatewithpredicate)
            - [7.3.59. Map.Project](#7359-mapproject)
            - [7.3.60. Map.ProjectWithPredicate](#7360-mapprojectwithpredicate)
            - [7.3.61. Map.FetchNearCacheInvalidationMetadata](#7361-mapfetchnearcacheinvalidationmetadata)
            - [7.3.62. Map.RemoveAll](#7362-mapremoveall)
            - [7.3.63. Map.AddNearCacheInvalidationListener](#7363-mapaddnearcacheinvalidationlistener)
            - [7.3.64. Map.FetchWithQuery](#7364-mapfetchwithquery)
            - [7.3.65. Map.EventJournalSubscribe](#7365-mapeventjournalsubscribe)
            - [7.3.66. Map.EventJournalRead](#7366-mapeventjournalread)
            - [7.3.67. Map.SetTtl](#7367-mapsetttl)
            - [7.3.68. Map.PutWithMaxIdle](#7368-mapputwithmaxidle)
            - [7.3.69. Map.PutTransientWithMaxIdle](#7369-mapputtransientwithmaxidle)
            - [7.3.70. Map.PutIfAbsentWithMaxIdle](#7370-mapputifabsentwithmaxidle)
            - [7.3.71. Map.SetWithMaxIdle](#7371-mapsetwithmaxidle)
            - [7.3.72. Map.ReplaceAll](#7372-mapreplaceall)
            - [7.3.73. Map.PutAllWithMetadata](#7373-mapputallwithmetadata)
        - [7.4. MultiMap](#74-multimap)
            - [7.4.1. MultiMap.Put](#741-multimapput)
            - [7.4.2. MultiMap.Get](#742-multimapget)
            - [7.4.3. MultiMap.Remove](#743-multimapremove)
            - [7.4.4. MultiMap.KeySet](#744-multimapkeyset)
            - [7.4.5. MultiMap.Values](#745-multimapvalues)
            - [7.4.6. MultiMap.EntrySet](#746-multimapentryset)
            - [7.4.7. MultiMap.ContainsKey](#747-multimapcontainskey)
            - [7.4.8. MultiMap.ContainsValue](#748-multimapcontainsvalue)
            - [7.4.9. MultiMap.ContainsEntry](#749-multimapcontainsentry)
            - [7.4.10. MultiMap.Size](#7410-multimapsize)
            - [7.4.11. MultiMap.Clear](#7411-multimapclear)
            - [7.4.12. MultiMap.ValueCount](#7412-multimapvaluecount)
            - [7.4.13. MultiMap.AddEntryListenerToKey](#7413-multimapaddentrylistenertokey)
            - [7.4.14. MultiMap.AddEntryListener](#7414-multimapaddentrylistener)
            - [7.4.15. MultiMap.RemoveEntryListener](#7415-multimapremoveentrylistener)
            - [7.4.16. MultiMap.Lock](#7416-multimaplock)
            - [7.4.17. MultiMap.TryLock](#7417-multimaptrylock)
            - [7.4.18. MultiMap.IsLocked](#7418-multimapislocked)
            - [7.4.19. MultiMap.Unlock](#7419-multimapunlock)
            - [7.4.20. MultiMap.ForceUnlock](#7420-multimapforceunlock)
            - [7.4.21. MultiMap.RemoveEntry](#7421-multimapremoveentry)
            - [7.4.22. MultiMap.Delete](#7422-multimapdelete)
            - [7.4.23. MultiMap.PutAll](#7423-multimapputall)
        - [7.5. Queue](#75-queue)
            - [7.5.1. Queue.Offer](#751-queueoffer)
            - [7.5.2. Queue.Put](#752-queueput)
            - [7.5.3. Queue.Size](#753-queuesize)
            - [7.5.4. Queue.Remove](#754-queueremove)
            - [7.5.5. Queue.Poll](#755-queuepoll)
            - [7.5.6. Queue.Take](#756-queuetake)
            - [7.5.7. Queue.Peek](#757-queuepeek)
            - [7.5.8. Queue.Iterator](#758-queueiterator)
            - [7.5.9. Queue.DrainTo](#759-queuedrainto)
            - [7.5.10. Queue.DrainToMaxSize](#7510-queuedraintomaxsize)
            - [7.5.11. Queue.Contains](#7511-queuecontains)
            - [7.5.12. Queue.ContainsAll](#7512-queuecontainsall)
            - [7.5.13. Queue.CompareAndRemoveAll](#7513-queuecompareandremoveall)
            - [7.5.14. Queue.CompareAndRetainAll](#7514-queuecompareandretainall)
            - [7.5.15. Queue.Clear](#7515-queueclear)
            - [7.5.16. Queue.AddAll](#7516-queueaddall)
            - [7.5.17. Queue.AddListener](#7517-queueaddlistener)
            - [7.5.18. Queue.RemoveListener](#7518-queueremovelistener)
            - [7.5.19. Queue.RemainingCapacity](#7519-queueremainingcapacity)
            - [7.5.20. Queue.IsEmpty](#7520-queueisempty)
        - [7.6. Topic](#76-topic)
            - [7.6.1. Topic.Publish](#761-topicpublish)
            - [7.6.2. Topic.AddMessageListener](#762-topicaddmessagelistener)
            - [7.6.3. Topic.RemoveMessageListener](#763-topicremovemessagelistener)
            - [7.6.4. Topic.PublishAll](#764-topicpublishall)
        - [7.7. List](#77-list)
            - [7.7.1. List.Size](#771-listsize)
            - [7.7.2. List.Contains](#772-listcontains)
            - [7.7.3. List.ContainsAll](#773-listcontainsall)
            - [7.7.4. List.Add](#774-listadd)
            - [7.7.5. List.Remove](#775-listremove)
            - [7.7.6. List.AddAll](#776-listaddall)
            - [7.7.7. List.CompareAndRemoveAll](#777-listcompareandremoveall)
            - [7.7.8. List.CompareAndRetainAll](#778-listcompareandretainall)
            - [7.7.9. List.Clear](#779-listclear)
            - [7.7.10. List.GetAll](#7710-listgetall)
            - [7.7.11. List.AddListener](#7711-listaddlistener)
            - [7.7.12. List.RemoveListener](#7712-listremovelistener)
            - [7.7.13. List.IsEmpty](#7713-listisempty)
            - [7.7.14. List.AddAllWithIndex](#7714-listaddallwithindex)
            - [7.7.15. List.Get](#7715-listget)
            - [7.7.16. List.Set](#7716-listset)
            - [7.7.17. List.AddWithIndex](#7717-listaddwithindex)
            - [7.7.18. List.RemoveWithIndex](#7718-listremovewithindex)
            - [7.7.19. List.LastIndexOf](#7719-listlastindexof)
            - [7.7.20. List.IndexOf](#7720-listindexof)
            - [7.7.21. List.Sub](#7721-listsub)
            - [7.7.22. List.Iterator](#7722-listiterator)
            - [7.7.23. List.ListIterator](#7723-listlistiterator)
        - [7.8. Set](#78-set)
            - [7.8.1. Set.Size](#781-setsize)
            - [7.8.2. Set.Contains](#782-setcontains)
            - [7.8.3. Set.ContainsAll](#783-setcontainsall)
            - [7.8.4. Set.Add](#784-setadd)
            - [7.8.5. Set.Remove](#785-setremove)
            - [7.8.6. Set.AddAll](#786-setaddall)
            - [7.8.7. Set.CompareAndRemoveAll](#787-setcompareandremoveall)
            - [7.8.8. Set.CompareAndRetainAll](#788-setcompareandretainall)
            - [7.8.9. Set.Clear](#789-setclear)
            - [7.8.10. Set.GetAll](#7810-setgetall)
            - [7.8.11. Set.AddListener](#7811-setaddlistener)
            - [7.8.12. Set.RemoveListener](#7812-setremovelistener)
            - [7.8.13. Set.IsEmpty](#7813-setisempty)
        - [7.9. FencedLock](#79-fencedlock)
            - [7.9.1. FencedLock.Lock](#791-fencedlocklock)
            - [7.9.2. FencedLock.TryLock](#792-fencedlocktrylock)
            - [7.9.3. FencedLock.Unlock](#793-fencedlockunlock)
            - [7.9.4. FencedLock.GetLockOwnership](#794-fencedlockgetlockownership)
        - [7.10. ExecutorService](#710-executorservice)
            - [7.10.1. ExecutorService.Shutdown](#7101-executorserviceshutdown)
            - [7.10.2. ExecutorService.IsShutdown](#7102-executorserviceisshutdown)
            - [7.10.3. ExecutorService.CancelOnPartition](#7103-executorservicecancelonpartition)
            - [7.10.4. ExecutorService.CancelOnMember](#7104-executorservicecancelonmember)
            - [7.10.5. ExecutorService.SubmitToPartition](#7105-executorservicesubmittopartition)
            - [7.10.6. ExecutorService.SubmitToMember](#7106-executorservicesubmittomember)
        - [7.11. AtomicLong](#711-atomiclong)
            - [7.11.1. AtomicLong.Apply](#7111-atomiclongapply)
            - [7.11.2. AtomicLong.Alter](#7112-atomiclongalter)
            - [7.11.3. AtomicLong.AddAndGet](#7113-atomiclongaddandget)
            - [7.11.4. AtomicLong.CompareAndSet](#7114-atomiclongcompareandset)
            - [7.11.5. AtomicLong.Get](#7115-atomiclongget)
            - [7.11.6. AtomicLong.GetAndAdd](#7116-atomiclonggetandadd)
            - [7.11.7. AtomicLong.GetAndSet](#7117-atomiclonggetandset)
        - [7.12. AtomicRef](#712-atomicref)
            - [7.12.1. AtomicRef.Apply](#7121-atomicrefapply)
            - [7.12.2. AtomicRef.CompareAndSet](#7122-atomicrefcompareandset)
            - [7.12.3. AtomicRef.Contains](#7123-atomicrefcontains)
            - [7.12.4. AtomicRef.Get](#7124-atomicrefget)
            - [7.12.5. AtomicRef.Set](#7125-atomicrefset)
        - [7.13. CountDownLatch](#713-countdownlatch)
            - [7.13.1. CountDownLatch.TrySetCount](#7131-countdownlatchtrysetcount)
            - [7.13.2. CountDownLatch.Await](#7132-countdownlatchawait)
            - [7.13.3. CountDownLatch.CountDown](#7133-countdownlatchcountdown)
            - [7.13.4. CountDownLatch.GetCount](#7134-countdownlatchgetcount)
            - [7.13.5. CountDownLatch.GetRound](#7135-countdownlatchgetround)
        - [7.14. Semaphore](#714-semaphore)
            - [7.14.1. Semaphore.Init](#7141-semaphoreinit)
            - [7.14.2. Semaphore.Acquire](#7142-semaphoreacquire)
            - [7.14.3. Semaphore.Release](#7143-semaphorerelease)
            - [7.14.4. Semaphore.Drain](#7144-semaphoredrain)
            - [7.14.5. Semaphore.Change](#7145-semaphorechange)
            - [7.14.6. Semaphore.AvailablePermits](#7146-semaphoreavailablepermits)
            - [7.14.7. Semaphore.GetSemaphoreType](#7147-semaphoregetsemaphoretype)
        - [7.15. ReplicatedMap](#715-replicatedmap)
            - [7.15.1. ReplicatedMap.Put](#7151-replicatedmapput)
            - [7.15.2. ReplicatedMap.Size](#7152-replicatedmapsize)
            - [7.15.3. ReplicatedMap.IsEmpty](#7153-replicatedmapisempty)
            - [7.15.4. ReplicatedMap.ContainsKey](#7154-replicatedmapcontainskey)
            - [7.15.5. ReplicatedMap.ContainsValue](#7155-replicatedmapcontainsvalue)
            - [7.15.6. ReplicatedMap.Get](#7156-replicatedmapget)
            - [7.15.7. ReplicatedMap.Remove](#7157-replicatedmapremove)
            - [7.15.8. ReplicatedMap.PutAll](#7158-replicatedmapputall)
            - [7.15.9. ReplicatedMap.Clear](#7159-replicatedmapclear)
            - [7.15.10. ReplicatedMap.AddEntryListenerToKeyWithPredicate](#71510-replicatedmapaddentrylistenertokeywithpredicate)
            - [7.15.11. ReplicatedMap.AddEntryListenerWithPredicate](#71511-replicatedmapaddentrylistenerwithpredicate)
            - [7.15.12. ReplicatedMap.AddEntryListenerToKey](#71512-replicatedmapaddentrylistenertokey)
            - [7.15.13. ReplicatedMap.AddEntryListener](#71513-replicatedmapaddentrylistener)
            - [7.15.14. ReplicatedMap.RemoveEntryListener](#71514-replicatedmapremoveentrylistener)
            - [7.15.15. ReplicatedMap.KeySet](#71515-replicatedmapkeyset)
            - [7.15.16. ReplicatedMap.Values](#71516-replicatedmapvalues)
            - [7.15.17. ReplicatedMap.EntrySet](#71517-replicatedmapentryset)
            - [7.15.18. ReplicatedMap.AddNearCacheEntryListener](#71518-replicatedmapaddnearcacheentrylistener)
            - [7.15.19. ReplicatedMap.PutAllWithMetadata](#71519-replicatedmapputallwithmetadata)
            - [7.15.20. ReplicatedMap.FetchEntryViews](#71520-replicatedmapfetchentryviews)
            - [7.15.21. ReplicatedMap.EndEntryViewIteration](#71521-replicatedmapendentryviewiteration)
        - [7.16. TransactionalMap](#716-transactionalmap)
            - [7.16.1. TransactionalMap.ContainsKey](#7161-transactionalmapcontainskey)
            - [7.16.2. TransactionalMap.Get](#7162-transactionalmapget)
            - [7.16.3. TransactionalMap.GetForUpdate](#7163-transactionalmapgetforupdate)
            - [7.16.4. TransactionalMap.Size](#7164-transactionalmapsize)
            - [7.16.5. TransactionalMap.IsEmpty](#7165-transactionalmapisempty)
            - [7.16.6. TransactionalMap.Put](#7166-transactionalmapput)
            - [7.16.7. TransactionalMap.Set](#7167-transactionalmapset)
            - [7.16.8. TransactionalMap.PutIfAbsent](#7168-transactionalmapputifabsent)
            - [7.16.9. TransactionalMap.Replace](#7169-transactionalmapreplace)
            - [7.16.10. TransactionalMap.ReplaceIfSame](#71610-transactionalmapreplaceifsame)
            - [7.16.11. TransactionalMap.Remove](#71611-transactionalmapremove)
            - [7.16.12. TransactionalMap.Delete](#71612-transactionalmapdelete)
            - [7.16.13. TransactionalMap.RemoveIfSame](#71613-transactionalmapremoveifsame)
            - [7.16.14. TransactionalMap.KeySet](#71614-transactionalmapkeyset)
            - [7.16.15. TransactionalMap.KeySetWithPredicate](#71615-transactionalmapkeysetwithpredicate)
            - [7.16.16. TransactionalMap.Values](#71616-transactionalmapvalues)
            - [7.16.17. TransactionalMap.ValuesWithPredicate](#71617-transactionalmapvalueswithpredicate)
            - [7.16.18. TransactionalMap.ContainsValue](#71618-transactionalmapcontainsvalue)
        - [7.17. TransactionalMultiMap](#717-transactionalmultimap)
            - [7.17.1. TransactionalMultiMap.Put](#7171-transactionalmultimapput)
            - [7.17.2. TransactionalMultiMap.Get](#7172-transactionalmultimapget)
            - [7.17.3. TransactionalMultiMap.Remove](#7173-transactionalmultimapremove)
            - [7.17.4. TransactionalMultiMap.RemoveEntry](#7174-transactionalmultimapremoveentry)
            - [7.17.5. TransactionalMultiMap.ValueCount](#7175-transactionalmultimapvaluecount)
            - [7.17.6. TransactionalMultiMap.Size](#7176-transactionalmultimapsize)
        - [7.18. TransactionalSet](#718-transactionalset)
            - [7.18.1. TransactionalSet.Add](#7181-transactionalsetadd)
            - [7.18.2. TransactionalSet.Remove](#7182-transactionalsetremove)
            - [7.18.3. TransactionalSet.Size](#7183-transactionalsetsize)
        - [7.19. TransactionalList](#719-transactionallist)
            - [7.19.1. TransactionalList.Add](#7191-transactionallistadd)
            - [7.19.2. TransactionalList.Remove](#7192-transactionallistremove)
            - [7.19.3. TransactionalList.Size](#7193-transactionallistsize)
        - [7.20. TransactionalQueue](#720-transactionalqueue)
            - [7.20.1. TransactionalQueue.Offer](#7201-transactionalqueueoffer)
            - [7.20.2. TransactionalQueue.Take](#7202-transactionalqueuetake)
            - [7.20.3. TransactionalQueue.Poll](#7203-transactionalqueuepoll)
            - [7.20.4. TransactionalQueue.Peek](#7204-transactionalqueuepeek)
            - [7.20.5. TransactionalQueue.Size](#7205-transactionalqueuesize)
        - [7.21. Cache](#721-cache)
            - [7.21.1. Cache.AddEntryListener](#7211-cacheaddentrylistener)
            - [7.21.2. Cache.Clear](#7212-cacheclear)
            - [7.21.3. Cache.RemoveAllKeys](#7213-cacheremoveallkeys)
            - [7.21.4. Cache.RemoveAll](#7214-cacheremoveall)
            - [7.21.5. Cache.ContainsKey](#7215-cachecontainskey)
            - [7.21.6. Cache.CreateConfig](#7216-cachecreateconfig)
            - [7.21.7. Cache.Destroy](#7217-cachedestroy)
            - [7.21.8. Cache.EntryProcessor](#7218-cacheentryprocessor)
            - [7.21.9. Cache.GetAll](#7219-cachegetall)
            - [7.21.10. Cache.GetAndRemove](#72110-cachegetandremove)
            - [7.21.11. Cache.GetAndReplace](#72111-cachegetandreplace)
            - [7.21.12. Cache.GetConfig](#72112-cachegetconfig)
            - [7.21.13. Cache.Get](#72113-cacheget)
            - [7.21.14. Cache.Iterate](#72114-cacheiterate)
            - [7.21.15. Cache.ListenerRegistration](#72115-cachelistenerregistration)
            - [7.21.16. Cache.LoadAll](#72116-cacheloadall)
            - [7.21.17. Cache.ManagementConfig](#72117-cachemanagementconfig)
            - [7.21.18. Cache.PutIfAbsent](#72118-cacheputifabsent)
            - [7.21.19. Cache.Put](#72119-cacheput)
            - [7.21.20. Cache.RemoveEntryListener](#72120-cacheremoveentrylistener)
            - [7.21.21. Cache.RemoveInvalidationListener](#72121-cacheremoveinvalidationlistener)
            - [7.21.22. Cache.Remove](#72122-cacheremove)
            - [7.21.23. Cache.Replace](#72123-cachereplace)
            - [7.21.24. Cache.Size](#72124-cachesize)
            - [7.21.25. Cache.AddPartitionLostListener](#72125-cacheaddpartitionlostlistener)
            - [7.21.26. Cache.RemovePartitionLostListener](#72126-cacheremovepartitionlostlistener)
            - [7.21.27. Cache.PutAll](#72127-cacheputall)
            - [7.21.28. Cache.IterateEntries](#72128-cacheiterateentries)
            - [7.21.29. Cache.AddNearCacheInvalidationListener](#72129-cacheaddnearcacheinvalidationlistener)
            - [7.21.30. Cache.FetchNearCacheInvalidationMetadata](#72130-cachefetchnearcacheinvalidationmetadata)
            - [7.21.31. Cache.EventJournalSubscribe](#72131-cacheeventjournalsubscribe)
            - [7.21.32. Cache.EventJournalRead](#72132-cacheeventjournalread)
            - [7.21.33. Cache.SetExpiryPolicy](#72133-cachesetexpirypolicy)
        - [7.22. XATransaction](#722-xatransaction)
            - [7.22.1. XATransaction.ClearRemote](#7221-xatransactionclearremote)
            - [7.22.2. XATransaction.CollectTransactions](#7222-xatransactioncollecttransactions)
            - [7.22.3. XATransaction.Finalize](#7223-xatransactionfinalize)
            - [7.22.4. XATransaction.Commit](#7224-xatransactioncommit)
            - [7.22.5. XATransaction.Create](#7225-xatransactioncreate)
            - [7.22.6. XATransaction.Prepare](#7226-xatransactionprepare)
            - [7.22.7. XATransaction.Rollback](#7227-xatransactionrollback)
        - [7.23. Transaction](#723-transaction)
            - [7.23.1. Transaction.Commit](#7231-transactioncommit)
            - [7.23.2. Transaction.Create](#7232-transactioncreate)
            - [7.23.3. Transaction.Rollback](#7233-transactionrollback)
        - [7.24. ContinuousQuery](#724-continuousquery)
            - [7.24.1. ContinuousQuery.PublisherCreateWithValue](#7241-continuousquerypublishercreatewithvalue)
            - [7.24.2. ContinuousQuery.PublisherCreate](#7242-continuousquerypublishercreate)
            - [7.24.3. ContinuousQuery.MadePublishable](#7243-continuousquerymadepublishable)
            - [7.24.4. ContinuousQuery.AddListener](#7244-continuousqueryaddlistener)
            - [7.24.5. ContinuousQuery.SetReadCursor](#7245-continuousquerysetreadcursor)
            - [7.24.6. ContinuousQuery.DestroyCache](#7246-continuousquerydestroycache)
        - [7.25. Ringbuffer](#725-ringbuffer)
            - [7.25.1. Ringbuffer.Size](#7251-ringbuffersize)
            - [7.25.2. Ringbuffer.TailSequence](#7252-ringbuffertailsequence)
            - [7.25.3. Ringbuffer.HeadSequence](#7253-ringbufferheadsequence)
            - [7.25.4. Ringbuffer.Capacity](#7254-ringbuffercapacity)
            - [7.25.5. Ringbuffer.RemainingCapacity](#7255-ringbufferremainingcapacity)
            - [7.25.6. Ringbuffer.Add](#7256-ringbufferadd)
            - [7.25.7. Ringbuffer.ReadOne](#7257-ringbufferreadone)
            - [7.25.8. Ringbuffer.AddAll](#7258-ringbufferaddall)
            - [7.25.9. Ringbuffer.ReadMany](#7259-ringbufferreadmany)
        - [7.26. DurableExecutor](#726-durableexecutor)
            - [7.26.1. DurableExecutor.Shutdown](#7261-durableexecutorshutdown)
            - [7.26.2. DurableExecutor.IsShutdown](#7262-durableexecutorisshutdown)
            - [7.26.3. DurableExecutor.SubmitToPartition](#7263-durableexecutorsubmittopartition)
            - [7.26.4. DurableExecutor.RetrieveResult](#7264-durableexecutorretrieveresult)
            - [7.26.5. DurableExecutor.DisposeResult](#7265-durableexecutordisposeresult)
            - [7.26.6. DurableExecutor.RetrieveAndDisposeResult](#7266-durableexecutorretrieveanddisposeresult)
        - [7.27. CardinalityEstimator](#727-cardinalityestimator)
            - [7.27.1. CardinalityEstimator.Add](#7271-cardinalityestimatoradd)
            - [7.27.2. CardinalityEstimator.Estimate](#7272-cardinalityestimatorestimate)
        - [7.28. ScheduledExecutor](#728-scheduledexecutor)
            - [7.28.1. ScheduledExecutor.Shutdown](#7281-scheduledexecutorshutdown)
            - [7.28.2. ScheduledExecutor.SubmitToPartition](#7282-scheduledexecutorsubmittopartition)
            - [7.28.3. ScheduledExecutor.SubmitToMember](#7283-scheduledexecutorsubmittomember)
            - [7.28.4. ScheduledExecutor.GetAllScheduledFutures](#7284-scheduledexecutorgetallscheduledfutures)
            - [7.28.5. ScheduledExecutor.GetStatsFromPartition](#7285-scheduledexecutorgetstatsfrompartition)
            - [7.28.6. ScheduledExecutor.GetStatsFromMember](#7286-scheduledexecutorgetstatsfrommember)
            - [7.28.7. ScheduledExecutor.GetDelayFromPartition](#7287-scheduledexecutorgetdelayfrompartition)
            - [7.28.8. ScheduledExecutor.GetDelayFromMember](#7288-scheduledexecutorgetdelayfrommember)
            - [7.28.9. ScheduledExecutor.CancelFromPartition](#7289-scheduledexecutorcancelfrompartition)
            - [7.28.10. ScheduledExecutor.CancelFromMember](#72810-scheduledexecutorcancelfrommember)
            - [7.28.11. ScheduledExecutor.IsCancelledFromPartition](#72811-scheduledexecutoriscancelledfrompartition)
            - [7.28.12. ScheduledExecutor.IsCancelledFromMember](#72812-scheduledexecutoriscancelledfrommember)
            - [7.28.13. ScheduledExecutor.IsDoneFromPartition](#72813-scheduledexecutorisdonefrompartition)
            - [7.28.14. ScheduledExecutor.IsDoneFromMember](#72814-scheduledexecutorisdonefrommember)
            - [7.28.15. ScheduledExecutor.GetResultFromPartition](#72815-scheduledexecutorgetresultfrompartition)
            - [7.28.16. ScheduledExecutor.GetResultFromMember](#72816-scheduledexecutorgetresultfrommember)
            - [7.28.17. ScheduledExecutor.DisposeFromPartition](#72817-scheduledexecutordisposefrompartition)
            - [7.28.18. ScheduledExecutor.DisposeFromMember](#72818-scheduledexecutordisposefrommember)
        - [7.29. DynamicConfig](#729-dynamicconfig)
            - [7.29.1. DynamicConfig.AddMultiMapConfig](#7291-dynamicconfigaddmultimapconfig)
            - [7.29.2. DynamicConfig.AddRingbufferConfig](#7292-dynamicconfigaddringbufferconfig)
            - [7.29.3. DynamicConfig.AddCardinalityEstimatorConfig](#7293-dynamicconfigaddcardinalityestimatorconfig)
            - [7.29.4. DynamicConfig.AddListConfig](#7294-dynamicconfigaddlistconfig)
            - [7.29.5. DynamicConfig.AddSetConfig](#7295-dynamicconfigaddsetconfig)
            - [7.29.6. DynamicConfig.AddReplicatedMapConfig](#7296-dynamicconfigaddreplicatedmapconfig)
            - [7.29.7. DynamicConfig.AddTopicConfig](#7297-dynamicconfigaddtopicconfig)
            - [7.29.8. DynamicConfig.AddExecutorConfig](#7298-dynamicconfigaddexecutorconfig)
            - [7.29.9. DynamicConfig.AddDurableExecutorConfig](#7299-dynamicconfigadddurableexecutorconfig)
            - [7.29.10. DynamicConfig.AddScheduledExecutorConfig](#72910-dynamicconfigaddscheduledexecutorconfig)
            - [7.29.11. DynamicConfig.AddQueueConfig](#72911-dynamicconfigaddqueueconfig)
            - [7.29.12. DynamicConfig.AddMapConfig](#72912-dynamicconfigaddmapconfig)
            - [7.29.13. DynamicConfig.AddReliableTopicConfig](#72913-dynamicconfigaddreliabletopicconfig)
            - [7.29.14. DynamicConfig.AddCacheConfig](#72914-dynamicconfigaddcacheconfig)
            - [7.29.15. DynamicConfig.AddFlakeIdGeneratorConfig](#72915-dynamicconfigaddflakeidgeneratorconfig)
            - [7.29.16. DynamicConfig.AddPNCounterConfig](#72916-dynamicconfigaddpncounterconfig)
            - [7.29.17. DynamicConfig.AddDataConnectionConfig](#72917-dynamicconfigadddataconnectionconfig)
            - [7.29.18. DynamicConfig.AddWanReplicationConfig](#72918-dynamicconfigaddwanreplicationconfig)
            - [7.29.19. DynamicConfig.AddUserCodeNamespaceConfig](#72919-dynamicconfigaddusercodenamespaceconfig)
            - [7.29.20. DynamicConfig.AddVectorCollectionConfig](#72920-dynamicconfigaddvectorcollectionconfig)
        - [7.30. FlakeIdGenerator](#730-flakeidgenerator)
            - [7.30.1. FlakeIdGenerator.NewIdBatch](#7301-flakeidgeneratornewidbatch)
        - [7.31. PNCounter](#731-pncounter)
            - [7.31.1. PNCounter.Get](#7311-pncounterget)
            - [7.31.2. PNCounter.Add](#7312-pncounteradd)
            - [7.31.3. PNCounter.GetConfiguredReplicaCount](#7313-pncountergetconfiguredreplicacount)
        - [7.32. CPGroup](#732-cpgroup)
            - [7.32.1. CPGroup.CreateCPGroup](#7321-cpgroupcreatecpgroup)
            - [7.32.2. CPGroup.DestroyCPObject](#7322-cpgroupdestroycpobject)
        - [7.33. CPSession](#733-cpsession)
            - [7.33.1. CPSession.CreateSession](#7331-cpsessioncreatesession)
            - [7.33.2. CPSession.CloseSession](#7332-cpsessionclosesession)
            - [7.33.3. CPSession.HeartbeatSession](#7333-cpsessionheartbeatsession)
            - [7.33.4. CPSession.GenerateThreadId](#7334-cpsessiongeneratethreadid)
        - [7.34. Sql](#734-sql)
            - [7.34.1. Sql.Execute_reserved](#7341-sqlexecute_reserved)
            - [7.34.2. Sql.Fetch_reserved](#7342-sqlfetch_reserved)
            - [7.34.3. Sql.Close](#7343-sqlclose)
            - [7.34.4. Sql.Execute](#7344-sqlexecute)
            - [7.34.5. Sql.Fetch](#7345-sqlfetch)
            - [7.34.6. Sql.MappingDdl](#7346-sqlmappingddl)
        - [7.35. CPSubsystem](#735-cpsubsystem)
            - [7.35.1. CPSubsystem.AddMembershipListener](#7351-cpsubsystemaddmembershiplistener)
            - [7.35.2. CPSubsystem.RemoveMembershipListener](#7352-cpsubsystemremovemembershiplistener)
            - [7.35.3. CPSubsystem.AddGroupAvailabilityListener](#7353-cpsubsystemaddgroupavailabilitylistener)
            - [7.35.4. CPSubsystem.RemoveGroupAvailabilityListener](#7354-cpsubsystemremovegroupavailabilitylistener)
            - [7.35.5. CPSubsystem.GetCPGroupIds](#7355-cpsubsystemgetcpgroupids)
            - [7.35.6. CPSubsystem.GetCPObjectInfos](#7356-cpsubsystemgetcpobjectinfos)
        - [7.36. CPMap](#736-cpmap)
            - [7.36.1. CPMap.Get](#7361-cpmapget)
            - [7.36.2. CPMap.Put](#7362-cpmapput)
            - [7.36.3. CPMap.Set](#7363-cpmapset)
            - [7.36.4. CPMap.Remove](#7364-cpmapremove)
            - [7.36.5. CPMap.Delete](#7365-cpmapdelete)
            - [7.36.6. CPMap.CompareAndSet](#7366-cpmapcompareandset)
            - [7.36.7. CPMap.PutIfAbsent](#7367-cpmapputifabsent)
        - [7.37. VectorCollection](#737-vectorcollection)
            - [7.37.1. VectorCollection.Put](#7371-vectorcollectionput)
            - [7.37.2. VectorCollection.PutIfAbsent](#7372-vectorcollectionputifabsent)
            - [7.37.3. VectorCollection.PutAll](#7373-vectorcollectionputall)
            - [7.37.4. VectorCollection.Get](#7374-vectorcollectionget)
            - [7.37.5. VectorCollection.Remove](#7375-vectorcollectionremove)
            - [7.37.6. VectorCollection.Set](#7376-vectorcollectionset)
            - [7.37.7. VectorCollection.Delete](#7377-vectorcollectiondelete)
            - [7.37.8. VectorCollection.SearchNearVector](#7378-vectorcollectionsearchnearvector)
            - [7.37.9. VectorCollection.Optimize](#7379-vectorcollectionoptimize)
            - [7.37.10. VectorCollection.Clear](#73710-vectorcollectionclear)
            - [7.37.11. VectorCollection.Size](#73711-vectorcollectionsize)
        - [7.38. Experimental](#738-experimental)
            - [7.38.1. Experimental.PipelineSubmit](#7381-experimentalpipelinesubmit)
        - [7.39. Jet](#739-jet)
            - [7.39.1. Jet.SubmitJob](#7391-jetsubmitjob)
            - [7.39.2. Jet.TerminateJob](#7392-jetterminatejob)
            - [7.39.3. Jet.GetJobStatus](#7393-jetgetjobstatus)
            - [7.39.4. Jet.GetJobIds](#7394-jetgetjobids)
            - [7.39.5. Jet.JoinSubmittedJob](#7395-jetjoinsubmittedjob)
            - [7.39.7. Jet.GetJobSubmissionTime](#7397-jetgetjobsubmissiontime)
            - [7.39.8. Jet.GetJobConfig](#7398-jetgetjobconfig)
            - [7.39.9. Jet.ResumeJob](#7399-jetresumejob)
            - [7.39.10. Jet.ExportSnapshot](#73910-jetexportsnapshot)
            - [7.39.11. Jet.GetJobSummaryList](#73911-jetgetjobsummarylist)
            - [7.39.12. Jet.ExistsDistributedObject](#73912-jetexistsdistributedobject)
            - [7.39.13. Jet.GetJobMetrics](#73913-jetgetjobmetrics)
            - [7.39.14. Jet.GetJobSuspensionCause](#73914-jetgetjobsuspensioncause)
            - [7.39.15. Jet.GetJobAndSqlSummaryList](#73915-jetgetjobandsqlsummarylist)
            - [7.39.16. Jet.IsJobUserCancelled](#73916-jetisjobusercancelled)
            - [7.39.17. Jet.UploadJobMetaData](#73917-jetuploadjobmetadata)
            - [7.39.18. Jet.UploadJobMultipart](#73918-jetuploadjobmultipart)
            - [7.39.19. Jet.AddJobStatusListener](#73919-jetaddjobstatuslistener)
            - [7.39.20. Jet.RemoveJobStatusListener](#73920-jetremovejobstatuslistener)
            - [7.39.21. Jet.UpdateJobConfig](#73921-jetupdatejobconfig)
    - [8. Copyright](#8-copyright)


## 1. Introduction
This document explains the new binary protocol that Hazelcast uses to communicate with the clients.
This document is not a guide to implement a client that will interact with Hazelcast; rather, it specifies the wire
data format for the messages exchanged between a client and a Hazelcast member node. Any client that wants to
communicate with the Hazelcast cluster should obey the data format and communication details explained in this document.

The protocol is designed to be strict enough to ensure standardization in the communication, but flexible enough
that developers may expand upon the protocol to implement custom features.

General guidelines:
- This document uses the terms MUST, MUST NOT, MAY, SHOULD, and SHOULD NOT as described in the [IETF RFC 2119](https://tools.ietf.org/html/rfc2119).
- Client refers to the entity which communicates with a Hazelcast member node.
- Member or server refers to the Hazelcast node to which the client connects.

## 2. Data Format Details
Hazelcast provides a communication interface to access distributed objects through client protocol. This interface is
a TCP socket listening for request messages. Currently, TCP socket communication is the only way a client can connect to
a member. The client MUST connect to the port that Hazelcast member is listening to for new connections. Because of
this, there is no fixed port to which the client must connect.

Protocol communication is built on sending and receiving messages. Client protocol defines a simple entity called
client message for communication. It is the only data format defined by this protocol.

### 2.1. Client Message
A client message is a transmission data unit composed of frames which are array of bytes. Its main purpose is to
encapsulate a unit of data to be transferred from one entity to another. It may represent a request, a response, or an
event response. A client message can be fragmented into multiple client messages and sent in order one-by-one. See the
[Client Message Fragmentation](#214-client-message-fragmentation) section for details.

#### 2.1.1. Frame
As said above, frames are building blocks of a client message. A frame is an array of bytes consisted of frame length,
flags and payload bytes as shown below.

| Frame Length | Flags | Payload |
| ------------ | ----  | ------- |
| int32 | uint16 | Payload bytes |

Frame length includes the length of itself, flags, and payload bytes. Hence, the minimum size of a frame is `6` bytes in
case of an empty payload (`4` bytes for frame length and `2` bytes for flags). Payload bytes store the actual
data carried over the frame. Frames must be in the little-endian order.

Flag bits have the structure shown below.

| Flag Bit | Name | Description |
| -------- | ---- | ----------- |
| 15 | BEGIN_FRAGMENT_FLAG | Used in message fragmentation |
| 14 | END_FRAGMENT_FLAG | Used in message fragmentation |
| 13 | IS_FINAL_FLAG | Set to 1 if the frame is the last frame of a client message |
| 12 | BEGIN_DATA_STRUCTURE_FLAG | Set to 1 if the frame is the begin frame of a custom type or list or map of variable sized type(s) |
| 11 | END_DATA_STRUCTURE_FLAG | Set to 1 if the frame is the end frame of a custom type or list or map of variable sized type(s) |
| 10 | IS_NULL_FLAG | Set to 1 if the frame represents a null payload |
| 9 | IS_EVENT_FLAG | Set to 1 if the frame is the initial frame of a client message that represents a event response from a member |
| 8 | BACKUP_AWARE_FLAG | Set to 1 if the client enabled receiving backup acks directly from members that backups are applied to |
| 7 | BACKUP_EVENT_FLAG | Set to 1 if the frame is the initial frame of a client message that represents a backup event response from a member |
| 6 to 0 | Reserved | Reserved for future usage |

#### 2.1.2. Initial Frame
Each client message starts with a special frame called the initial frame. It is special in the sense that it includes all the
fix sized parameters of a client message. Fix sized parameters are parameters of a request, a response, or an event response
message in which the sizes of the parameter in bytes can be known in advance. These types of parameters are listed below.

| Type | Size in bytes |
| ---- | ------------- |
| byte (int8 or uint8) | 1 |
| boolean | 1 |
| int (int32 or uint32) | 4 |
| long (int64 or uint64) | 8 |
| float | 4 |
| double | 8 |
| UUID* | 17 |

> *: UUID is described by two longs. Since UUID can be null, a boolean flag is also used to distinguish null UUIDs from non-null ones. That makes the length 17 bytes (1 + 8 + 8) in total.

The overall structure of the initial frame is shown below.

For requests and event responses, the overall structure of the initial frame is shown below.

| Frame length | Flags | Message type | Correlation ID | Partition ID | Fix sized parameter 1 | Fix sized parameter 2 | ... | Fix sized parameter n |
| ------------ | ----- | ------------ | -------------- | ------------ | --------------------- | --------------------- | --- | --------------------- |
| int32 | uint16 | int32 | int64 | int32 | Parameter 1 bytes | Parameter 2 bytes | ... | Parameter n bytes |

For responses, the overall structure of the initial frame is shown below.

| Frame length | Flags | Message type | Correlation ID | Backup Acks Count | Fix sized parameter 1 | Fix sized parameter 2 | ... | Fix sized parameter n |
| ------------ | ----- | ------------ | -------------- | ----------------- | --------------------- | --------------------- | --- | --------------------- |
| int32 | uint16 | int32 | int64 | uint8 | Parameter 1 bytes | Parameter 2 bytes | ... | Parameter n bytes |

Unfragmented client messages must have their `BEGIN_FRAGMENT_FLAG` and `END_FRAGMENT_FLAG` bits set to `1` in
their initial frames.

For the details of frame length and flags, see the section [above](#211-frame).

Payload bytes of the initial frame consists of message type, correlation ID, partition ID, or the backup acks count
depending on the message type and fix sized parameters.

##### 2.1.2.1. Message Type
Message type corresponds to a unique operation of a distributed object such as `Map.Put` request, `List.Get` response or
an event response for a registered listener.

| Message type byte | Description |
| ----------------- | ----------- |
| 0 | Unused, set to 0 |
| 1 | Service ID |
| 2 | Method ID |
| 3 | Request, response or event response ID |

Service ID represents the unique ID assigned to managed services provided by Hazelcast such as `Map`, `List`,
`Client` etc. It is in the range of `0` to `255`.

Method ID represents the unique IDs of methods provided by the service. It is in the range of `1` to `255`.

The last bit of the message type represents whether this client message is a request, a response, or an event response.
It is equal to `0` for requests, `1` for responses, and `2` plus event ID for event responses.

For example:
- `0x00010200` is the message type for the request (`00`) for the `Get` method (`02`) of the `Map` service (`01`).
- `0x00050F01` is the message type for the response (`01`) for the `Get` method (`0F`) of the `List` service (`05`).
- `0x00011C02` is the message type for the event response (`02`) for the `AddEntryListener` method (`1C`) of the `Map` service (`01`).

For the error messages that are sent by the member node to the client, the message type is set to `0x00000000`.

A full list of message types can be found in the [Protocol Messages](#7-protocol-messages) section.

If the Hazelcast member receives a message with an unsupported message type, it will return the `UNSUPPORTED_OPERATION`
error to the client with the message type of `0x00000000`. The client is guaranteed to receive only the messages listed
in the [Protocol Messages](#7-protocol-messages) and the error messages.

The details of the different message types are described in the next sections.

##### 2.1.2.1.1. Request Message Type
Each distributed object defines various operations. Each operation corresponds to a well-defined request message to
be sent to the cluster. For each request message, the client will get a response message from the cluster. Request messages
MUST be sent from the client to the server.

The request parameters are binary encoded entirely within the payload bytes of the frames that constitute the client message.

##### 2.1.2.1.2. Response Message Type
Once a request is received and processed on the member side, the member produces a response message and sends it to
the client. Each request message type defines a response message that can be sent. The correlation ID relates all instances
of the response messages to their requests.

The response parameters are binary encoded entirely within the payload bytes of the frames that constitute the client messages.

##### 2.1.2.1.3. Event Response Message Type
An event response message is a special kind of response message. A client can register to a specific listener by
sending a request message with the message type of adding a listener. When an event is triggered that the client is
listening for, the member will send a message to the client using the same correlation ID as the original request message.
The payload bytes of the frames of the event message carries the specific event object. The possible event message types
for a registration request are documented in the `Event Message` section of each request in the
[Protocol Messages](#7-protocol-messages) section.

For these messages, `IS_EVENT_FLAG` bit of the initial frame of the client message is set to `1`.

The member will continue to send the client event updates until the client unregisters from that event or the connection
is broken.

##### 2.1.2.1.4. Error Message Type
The member may return an error response to the client for the request it made. For this message, the message type is set
to `0x00000000`. The payload of the member's response message contains the error message along with the error code.
You may choose to provide the error codes directly to the user or you may use some other technique, such as exceptions,
to delegate the error to the user. See the `ErrorHolder` custom type and the list of [Error Codes](#58-error-codes) for details.

##### 2.1.2.2. Correlation ID
This ID correlates the request to responses. It should be unique to identify one message in the communication. This ID
is used to track the request-response cycle of a client operation. Members send response messages with the same ID as
the request message. The uniqueness is per connection. If the client receives the response to a request and the request
is not a multi-response request (i.e. not a request for event transmission), then the correlation ID for the request can
be reused by the subsequent requests. Note that once a correlation ID is used to register for an event, it SHOULD NOT
be used again unless the client unregisters (stops listening) for that event.

##### 2.1.2.3. Partition ID
The partition ID defines the partition against which the operation is executed. This information tells the
client which member handles which partition. The client can use this information to send requests to the responsible
member directly for processing. The client gets this information from the `PartitionsView` event of the
`AddClusterViewListener` request. (see the [Protocol Messages](#7-protocol-messages))

To determine the partition ID of an operation, the client needs to compute the Murmur Hash (version 3, 32-bit, see
[https://en.wikipedia.org/wiki/MurmurHash](https://en.wikipedia.org/wiki/MurmurHash) and
[https://github.com/aappleby/smhasher/wiki/MurmurHash3](https://github.com/aappleby/smhasher/wiki/MurmurHash3)) of a
certain byte-array (which is identified for each message in the description section) and take the modulus of the result
over the total number of partitions. The seed for the Murmur Hash SHOULD be `0x0100193`. Most operations with a key
parameter use the key parameter byte-array as the data for the hash calculation.

Some operations are not required to be executed on a specific partition but can be run on a global execution pool. For
these operations, the partition ID is set to a negative value. No hash calculation is required in this case.

##### 2.1.2.4 Backup Acks Count
When the client performs an operation on a distributed object that requires backups to be created when a change is made,
the client only receives the response of the operation when acks from the member nodes that participated in the
backup process are seen.

Hazelcast offers two different ways to perform operations that involve backups.

If the client is a [smart client](#61-smart-client-and-unisocket-client), it can mark the requests it sends as backup
aware by setting the `BACKUP_AWARE_FLAG` to `1`. When a Hazelcast member receives such a request, it sends a response
message that carries information about how many backup operations must be performed along with the actual response in
this part of the initial frame. In this case, the client is notified about the successful backups with event responses
coming from the member nodes that created the backups in their partitions. To do so, the client must register listeners to
all member nodes that it is connected to using the `LocalBackupListener` message. The client SHOULD wait until it
receives event responses marked with `BACKUP_EVENT_FLAG` from that many Hazelcast member nodes before resolving the
response of the request.

However, if the client is a [unisocket client](#61-smart-client-and-unisocket-client) or the requests going out from
it are not marked with the `BACKUP_AWARE_FLAG`, the member node that receives the request from the client only sends
the response back when it receives acks from other cluster members which are participated in the backup process.

The former way is faster in the sense that it results in fewer serial network hops.

#### 2.1.3. Encoding of Variable Sized Parameters

The parameters of the client message that have variable size, that are not listed in the fix sized types described
in the [Initial Frame](#212-initial-frame) section, such as string, list of primitive or custom types, etc. are
encoded following the initial frame in their respective frames. A variable sized parameter can be encoded into one or more
frames based on its type. For the sections below, the following special frames will be used while describing the encoding
process of the variable sized parameters.

- `NULL_FRAME`: A frame that has `1` in its `IS_NULL_FLAG` bit. It is used to represent parameters that have null values.
It has empty payload.
- `BEGIN_FRAME`: A frame that has `1` in its `BEGIN_DATA_STRUCTURE_FLAG` bit. It is used to mark the beginning of the
parameter encodings that cannot fit into a single frame. It has empty payload bytes.
- `END_FRAME`: A frame that has `1` in its `END_DATA_STRUCTURE_FLAG` bit. It is used to mark the ending of the parameter
encodings that cannot fit into a single frame. It has empty payload bytes.

For the encodings described below, if the parameter is of a variable sized type and its value is null, it is encoded as
`NULL_FRAME`.

##### 2.1.3.1. Encoding of String Parameters
Each string parameter of the client message can be encoded into its own single frame. String parameters are expected to
be encoded according to UTF-8 standard described in the [RFC 3629](https://tools.ietf.org/html/rfc3629). Encoded string data must be placed in the payload
bytes of the frame. Below is the sample structure of a string frame.

| Frame length | Flags | UTF-8 encoded string data |
| ------------ | ----- | ------------------------- |
| int32 | uint16 | UTF-8 encoded string bytes |

##### 2.1.3.2. Encoding of Custom Type Parameters
Custom types, which are the parameters of the client messages that consist of other fix or variable sized parameters
are encoded in between `BEGIN_FRAME` and `END_FRAME`. Overall, the structure of custom type encodings is shown below.

| `BEGIN_FRAME` | Payload Frame 1 | Payload Frame 2 | ... | Payload Frame n | `END_FRAME` |
| ------------- | --------------- | --------------- | --- | --------------- | ----------- |

`BEGIN_FRAME` and `END_FRAME` are used to identify the boundaries of different custom type encodings. While reading
frames of a client message, when a `BEGIN_FRAME` is encountered, it means that the custom type encoding is started and
it is safe to read frames until the `END_FRAME` is encountered. All the frames in between those two will carry the
actual data stored inside the custom type.

Payload frames follow a similar schema to the initial frame and variable sized data frame structure described above. All
the fix sized parameters of the custom object are encoded in the initial payload frame that comes after the `BEGIN_FRAME`
and all the other variable sized or custom parameters are encoded in the following payload frames in the same way
described in the [Encoding of Variable Sized Parameters](#213-encoding-of-variable-sized-parameters) section. Therefore,
each custom type encoding consists of at least three and possibly more frames depending on the types of the parameters
of the custom object.

For example, if the custom type has the parameters of integer, long, string, and another custom type that has
boolean and string parameters, then the encoded structure of the custom object will be as below.

| Frame | Description |
| ----- | ----------- |
| `BEGIN_FRAME` | `BEGIN_FRAME` of the custom type |
| Payload frame for the fix sized parameters | Payload frame for the integer and long parameters |
| Payload frame for the var sized parameter | Payload frame for the string parameter |
| `BEGIN_FRAME` | `BEGIN_FRAME` of the custom type parameter |
| Payload frame for the fix sized parameter | Payload frame for the boolean parameter of the custom type parameter |
| Payload frame for the var sized parameter | Payload frame for the string parameter of the custom type parameter |
| `END_FRAME` | `END_FRAME` for the custom type parameter |
| `END_FRAME` | `END_FRAME` for the custom type |

As depicted above, fix sized parameters of the custom type which are integer and long parameters, are encoded in the initial
frame that follows the `BEGIN_FRAME` of the custom type. Then, the payload frame for the string parameter comes. It is encoded
in the same way described in the [Encoding of String Parameters](#2131-encoding-of-string-parameters) section.
Custom types can also contain other custom type parameters. They are encoded in the same way as described at the
beginning of the section. Payload frames of the inner custom type, which are the frames for the boolean parameter and the
string parameter, are encoded in between its respective `BEGIN_FRAME` and `END_FRAME`. Finally, the `END_FRAME` at the
end signals the finish of the custom type encoding.

##### 2.1.3.3. Encoding of List Parameters

Client messages may also contain a list of fix sized or variable sized types. The encoding of the list frames changes
according to the type of the list elements.

##### 2.1.3.3.1. Encoding of List of Fix Sized Parameters

Since the byte size of the fix sized parameters and the element count of the list can be known in advance, the content
of the list can be fit into a single frame. For these types of lists, payload size is calculated as
`ELEMENT_COUNT * ELEMENT_SIZE_IN_BYTES` and elements are encoded at the offsets depending on their indexes on lists.
Assuming zero-based indexing, element offsets can be calculated as `ELEMENT_INDEX * ELEMENT_SIZE_IN_BYTES`.

For example, a list of integers can be encoded into a single frame as follows:

| Frame length | Flags | int-0 | int-1 | ... | int-n |
| ------------ | ----- | ----- | ----- | --- | ----- |
| int32 | uint16 | int32 | int32 | ... | int32 |

Due to member-side technical restrictions, writing the elements of a list into a single frame puts an upper limit on
the maximum number of elements that the list contains. The number of elements that can be fit into a single frame can
be calculated as `(2^31 - 6) / ELEMENT_SIZE_IN_BYTES`. For example, for int64, a maximum of `268435455` (around `268` million)
entries per list is supported by the protocol.

##### 2.1.3.3.2. Encoding of List of Variable Sized Parameters
Lists of variable sized parameters, just like [custom type parameters](#2132-encoding-of-custom-type-parameters), are encoded in
between `BEGIN_FRAME` and `END_FRAME`. Each element of the list is encoded in their respective frames consecutively
following the `BEGIN_FRAME`. Depending on the type of list elements, each element may be encoded into one or more
frames. In fact, the encoding of a list of variable sized parameters is very similar to the encoding of the custom types.

For example, a list of string objects can be encoded as follows:

| `BEGIN_FRAME` | string-0 | string-1 | ... | string-n | `END_FRAME` |
| ------------- | -------- | -------- | --- | -------- | ----------- |
| Begin frame of the list | Frame containing UTF-8 encoded bytes of string-0 | Frame containing UTF-8 encoded bytes of string-1 | ... | Frame containing UTF-8 encoded bytes of string-n | End frame of the list |

Note that, elements of the list must be of the same type.

##### 2.1.3.4. Encoding of Map Parameters
Map parameters can be encoded in different ways depending on the types of keys and values.

If both are fix sized parameters as described above, map entries can be encoded into a single frame since the size of a
map entry can be known in advance. For these map entries, the payload size of the frame can be calculated as
`ENTRY_COUNT * (SIZE_OF_THE_KEY + SIZE_OF_THE_VALUE)`. Map entries are encoded in the offset positions depending on
their iteration order. The offset of the keys and values can be calculated as `ENTRY_INDEX * (SIZE_OF_THE_KEY + SIZE_OF_THE_VALUE)`
and `ENTRY_INDEX * (SIZE_OF_THE_KEY + SIZE_OF_THE_VALUE) + SIZE_OF_THE_KEY` respectively, assuming zero-based indexing.

For example, map entries of int32 to int64 mappings can be encoded as below.

| Frame length | Flags | int32-0 | int64-0 | int32-1 | int64-1 | ... | int32-n | int64-n |
| ------------ | ----- | ------- | ------- | ------- | ------- | --- | ------- | ------- |
| int32 | uint16 | int32 | int64 | int32 | int64 | ... | int32 | int64 |

If one of them is fix sized and the other is variable sized, map entries are encoded in between
`BEGIN_FRAME` and `END_FRAME`. Each key or value of the entry set that is variable sized is encoded in its respective
frames consecutively following the `BEGIN_FRAME`. As described above, this encoding may result in one or more frames
depending on the type of the variable sized key or value. Each key or value of the entry set that is fix sized is
encoded into a single frame as described in the [Encoding of List of Fix Sized Parameters](#21331-encoding-of-list-of-fix-sized-parameters) section.

For example, a map of string to int32 can be encoded as below.

| `BEGIN_FRAME` | string-0 | string-1 | ... | string-n | list of int32s | `END_FRAME` |
| ------------- | -------- | -------- | --- | -------- | -------------- | ----------- |
| Begin frame of the map entries | Frame containing UTF-8 encoded bytes of string-0 (key-0) | Frame containing UTF-8 encoded bytes of string-1 (key-1) | ... | Frame containing UTF-8 encoded bytes of string-n (key-n) | Frame containing list of int32s (values) | End frame of the map entries |

However, if both of them are variable sized, map entries are encoded in between `BEGIN_FRAME` and `END_FRAME`.
Each key or value of the entry set is encoded in its respective frames consecutively following the `BEGIN_FRAME`.

For example, a map of string to list of int32s can be encoded as below.

| `BEGIN_FRAME` | string-0 | list of int32-0 | string-1 | list of int32-1 | ... | string-n | list of int32-n | `END_FRAME` |
| ------------- | -------- | ---------------- | -------- | --------------- | --- | -------- | --------------- | ----------- |
| Begin frame of the map entries | Frame containing UTF-8 encoded bytes of string-0 (key-0) | Frame containing list of int32-0 (value-0) | Frame containing UTF-8 encoded bytes of string-1 (key-1) | Frame containing list of int32-1 (value-1) | ... | Frame containing UTF-8 encoded bytes of string-n (key-n) | Frame containing list of int32-n (value-n) | End frame of the map entries |

### 2.1.4. Client Message Fragmentation
A fragment is a part of a client message where the client message is too large and it is split into multiple client messages.
It is used to interleave large client messages so that small but urgent client messages can be sent without waiting for the transmission
of the large client message.

Fragmentation is handled through `BEGIN_FRAGMENT_FLAG` and `END_FRAGMENT_FLAG` bits of the frame flags.
Unfragmented messages have `1` in both flag bits. For fragmented client messages, the first fragment has `1` in
`BEGIN_FRAGMENT_FLAG` and `0` in `END_FRAGMENT_FLAG`, the last fragment has `0` in `BEGIN_FRAGMENT_FLAG` and `1` in
`END_FRAGMENT_FLAG` and middle fragments have `0` in both of the flag bits.

Fragments of different client messages are identified by the int64 fragment IDs. Fragment ID is encoded into the payload bytes.

Initial frames of the fragmented client messages have the following structure.

**First Fragment Initial Frame**

| Frame length | Flags | Payload |
| ------------ | ----- | ------- |
| Frame length | BEGIN_FRAGMENT_FLAG = 1, END_FRAGMENT_FLAG = 0 | Fragment ID |
| int32 | uint16 | int64 |

**Middle Fragment Initial Frame**

| Frame length | Flags | Payload |
| ------------ | ----- | ------- |
| Frame length | BEGIN_FRAGMENT_FLAG = 0, END_FRAGMENT_FLAG = 0 | Fragment ID |
| int32 | uint16 | int64 |

**Last Fragment Initial Frame**

| Frame length | Flags | Payload |
| ------------ | ----- | ------- |
| Frame length | BEGIN_FRAGMENT_FLAG = 0, END_FRAGMENT_FLAG = 1 | Fragment ID |
| int32 | uint16 | int64 |

Then, visual representation of the possible fragments of a client message with N frames can be as below:

**First Fragment**

| First Fragment Initial Frame | client message - 1st frame | client message - 2nd frame | ... | client message - ith frame |
| ---------------------------- | -------------------------- | -------------------------- | --- | -------------------------- |

**Middle Fragments**

| Middle Fragment Initial Frame | client message - (i+1)th frame | client message - (i+2)th frame | ... | client message - jth frame |
| ----------------------------- | ------------------------------ | ------------------------------ | --- | -------------------------- |

**Last Fragment**

| Last Fragment Initial Frame | client message - (j+1)th frame | client message - (j+2)th frame | ... | client message - nth frame |
| --------------------------- | ------------------------------ | ------------------------------ | --- | -------------------------- |

### 2.1.5. Client Message Boundaries
As described in the [Initial Frame](#212-initial-frame) and [Client Message Fragmentation](#214-client-message-fragmentation) sections,
the initial frame of the client messages can be identified with the `BEGIN_FRAGMENT_FLAG` and `END_FRAGMENT_FLAG` bits.

The last frame of a client message can be identified by checking the `IS_FINAL_FLAG` bit. If set to `1`, it signals that the client
message is ended.

### 2.1.6. Backward Compatibility of the Client Messages
Hazelcast Open Binary Protocol guarantees backward compatibility for all major 2.x versions. Therefore, developments done in the
protocol MUST NOT result in deletion of services, methods, or any parameters. However, new services, methods, or parameters MAY be added.

For the addition of fix sized parameters to service methods, additional parameters can be detected by checking the
frame length of the initial frame. An old reader reads and uses old parameters and simply skips the bytes that contain
the additional parameters.

On the other hand, the addition of variable sized parameters can be detected using the `END_FRAME`. An old reader reads
and uses old frames and simply skips the additional frames until it detects the `END_FRAME`.

### 2.1.7. Augmented Backus–Naur Format Representation of the Client Messages
Below is the representation of the client messages used within the protocol as described with the rules defined in
[RFC 5234](https://tools.ietf.org/html/rfc5234) that specifies the Augmented Backus–Naur format.
```
client-message                 = initial-frame *var-sized-param
initial-frame                  = request-initial-frame / response-initial-frame
request-initial-frame          = frame-header message-type correlation-id partition-id *fix-sized-param
response-initial-frame         = normal-response-initial-frame / event-response-initial-frame
normal-response-initial-frame  = frame-header message-type correlation-id backup-acks-count *fix-sized-param
event-response-initial-frame   = frame-header message-type correlation-id partition-id *fix-sized-param

frame-header                   = frame-length flags
frame-length                   = int32
message-type                   = int32
correlation-id                 = int64
partition-id                   = int32
backup-acks-count              = int8

var-sized-param                = single-frame-param / custom-type-param / list-param / map-param / null-frame
list-param                     = var-sized-list / fix-sized-list
map-param                      = fix-sized-to-fix-sized-map / var-sized-to-var-sized-map /
                               / fix-sized-to-var-sized-map / var-sized-to-fix-sized-map

var-sized-list                 = begin-frame *var-sized-param end-frame ; All elements should be of same type
fix-sized-list                 = frame-header *fix-sized-param ; All elements should be of same type

fix-sized-to-fix-sized-map     = frame-header *fix-sized-entry
fix-sized-entry                = fix-sized-param fix-sized-param ; Key and value pairs
var-sized-to-var-sized-map     = begin-frame *var-sized-entry end-frame
var-sized-entry                = var-sized-param var-sized-param ; Key and value pairs
fix-sized-to-var-sized-map     = begin-frame *var-sized-entry fix-sized-list end-frame ; Values as list of frames, keys as a single frame
var-sized-to-fix-sized-map     = begin-frame *var-sized-entry fix-sized-list end-frame ; Keys as list of frames, values as a single frame

single-frame-param             = frame-header *OCTET ; For String, Data, ByteArray types. Strings must be encoded as UTF-8
custom-type-param              = custom-type-begin-frame *1custom-type-initial-frame *var-sized-param end-frame
custom-type-begin-frame        = begin-frame / frame-header *fix-sized-param ; Fix sized params might be pigybacked to begin frame
custom-type-initial-frame      = frame-header *fix-sized-param

null-frame                     = frame-header ; IS_NULL_FLAG is set to one
begin-frame                    = frame-header ; BEGIN_DATA_STRUCTURE_FLAG is set to one
end-frame                      = frame-header ; END_DATA_STRUCTURE_FLAG is set to one

flags                          = begin-fragment end-fragment is-final begin-data-structure end-data-structure is-null is-event backup-aware backup-event 7reserved
begin-fragment                 = BIT ; Used in message fragmentation
end-fragment                   = BIT ; Used in message fragmentation
is-final                       = BIT ; Set to 1 if the frame is the last frame of a client message
begin-data-structure           = BIT ; Set to 1 if the frame is the begin frame of a custom type or list of variable sized types
end-data-structure             = BIT ; Set to 1 if the frame is the end frame of a custom type or list of variable sized types
is-null                        = BIT ; Set to 1 if the frame represents a null parameter
backup-aware                   = BIT ; Set to 1 if the client enabled receiving backup acks directly from members that backups are applied to
backup-event                   = BIT ; Set to 1 if the frame is the initial frame of a client message that represents a backup event response from a member
reserved                       = BIT ; Reserved for future usage

fix-sized-param                = *OCTET / boolean / int8 / int16 / int32 / int64 / UUID
boolean                        = %x00 / %x01
int8                           = 8BIT
int16                          = 16BIT
int32                          = 32BIT
int64                          = 64BIT
UUID                           = boolean int64 int64 ; Is null flag + most significant bits + least significant bits
```

For the fragmented client messages, the ABNF definition is below.

```
fragmented-message = begin-fragment *middle-fragment end-fragment
begin-fragment     = frame-header fragment-id 1*frame ; begin-fragment is set to 1, end-fragment is set to 0, is_final of last frame set to 1
middle-fragment    = frame-header fragment-id 1*frame ; begin-fragment is set to 0, end-fragment is set to 0, is_final of last frame set to 1
end-fragment       = frame-header fragment-id 1*frame ; begin-fragment is set to 0, end-fragment is set to 1, is_final of last frame set to 1

frame              = initial-frame / single-frame-param / custom-type-begin-frame / custom-type-initial-frame
                   / fix-sized-list / fix-sized-to-fix-sized-map / begin-frame / end-frame / null-frame
```

## 3. Client Protocol Data Types

| Type | Description | Size | Min Value | Max Value |
| ---- | ----------- | ---- | --------- | --------- |
| uint8 | unsigned 8 bit integer | 8 bit | 0 | 2^8 - 1 |
| uint16 | unsigned 16 bit integer | 16 bit | 0 | 2^16 - 1 |
| uint32 | unsigned 32 bit integer | 32 bit | 0 | 2^32 - 1 |
| uint64 | unsigned 64 bit integer | 64 bit | 0 | 2^64 - 1 |
| int8 | signed 8 bit integer in 2's complement | 8 bit | -2^7 | 2^7 - 1 |
| int16 | signed 16 bit integer in 2's complement | 16 bit | -2^15 | 2^15 - 1 |
| int32 | signed 32 bit integer in 2's complement  | 32 bit | -2^31 | 2^31 - 1 |
| int64 | signed 64 bit integer in 2's complement | 64 bit | -2^63 | 2^63 - 1 |
| float | single precision IEEE 754 floating point number | 32 bit | -1 * (2 - 2^(-23)) * 2^127  | (2 - 2^(-23)) * 2^127 |
| double | double precision IEEE 754 floating point number | 64 bit | -1 * (2 - 2^(-52)) * 2^1023 |  (2 - 2^(-52)) * 2^1023 |
| boolean | same as uint8 with special meanings. 0 is "false", any other value is "true" | 8 bit | | |
| String | String encoded as a byte-array with UTF-8 encoding as described in [RFC 3629](https://tools.ietf.org/html/rfc3629) | variable | | |
| Data | Basic unit of Hazelcast serialization that stores the binary form of a serialized object | variable | | |
| ByteArray | Array of bytes | variable | | |

Data types are consistent with those defined in The Open Group Base Specification Issue 7 IEEE Std 1003.1, 2013 Edition.
Data types are in **Little Endian** format.

## 4. Connection Guide

### 4.1. Opening a Connection
TCP socket communication is used for client-to-member communication. Each member has a socket listening for incoming connections.

As the first step of client-to-member communication, the client MUST open a TCP socket connection to the member.

A client needs to establish a single connection to each member node if it is a smart client. If it is a unisocket client,
a single connection is enough for a particular client. For details, see [Smart Client versus Unisocket Client](#61-smart-client-and-unisocket-client).

### 4.2. Connection Initialization
After successfully connecting to the member TCP socket, the client MUST send three bytes of initialization data to identify
the connection type to the member.

For any client, the three byte initializer data is [`0x43`, `0x50`, `0x32`], which is the string `CP2` in UTF-8 encoding.

### 4.3. Authentication
The first message sent through an initialized connection must be an authentication message. Any other type of message
will fail with an authorization error unless the authentication is complete.

Upon successful authentication, the client will receive a response from the member with the member's IP address, UUID
that uniquely identifies the member, and cluster UUID along with the other response parameters described
in `Client.Authentication` message. The status parameter in the authentication response should be checked for the
authentication status.

There are four possible statuses:

- `0`: Authentication is successful.
- `1`: Credentials failed. The provided credentials (e.g. cluster name, username, or password) are incorrect.
- `2`: Serialization version mismatch. The requested serialization version and the serialization version used on the member side
are different. The client gets the member's serialization version from the `serverHazelcastVersion` parameter of the response.
It is suggested that the client tries to reconnect using the matching serialization version assuming that the client
implements the version for serialization.
- `3`: The client is not allowed in the cluster. It might be the case that client is blacklisted from the cluster.

There are two types of authentications:

- Username/Password authentication: `Client.Authentication` message is used for this authentication type which contains
username and password for the client (if present) along with the cluster name.
- Custom credentials authentication: `Client.CustomAuthentication` message is used for this authentication type. Custom
authentication credentials are sent as a byte-array.

### 4.4. Communication

After successful authentication, a client may send request messages to the member to access distributed objects
or perform other operations on the cluster. This step is the actual communication step.

Once connected, a client can do the following:
1. Send periodic updates.
2. Get updates on cluster state view which consists of partition table and member list.
3. Send operation messages and receive responses.

All request messages will be sent to the member and all responses and event responses will be sent to the client.

See [Protocol Messages](#7-protocol-messages) for details.

### 4.5. Closing Connections
To end the communication, the network socket that was opened should be closed. This will
result in releasing resources on the member side specific to this connection.

## 5. Requests and Responses
### 5.1. Distributed Objects
To access distributed object information, use the `GetDistributedObject` message.

To add a listener for adding distributed objects, use the `AddDistributedObjectListener` message.

To remove a formerly added listener, use the `RemoveDistributedObjectListener` message.

### 5.2. Operation Messages And Responses
Operational messages are the messages where a client can expect exactly one response for a given request. The client
knows which request the response correlates to via the correlation ID. An example of one of these operations is a
`Map.Put` operation.

To execute a particular operation, set the message type ID to the corresponding operation type and encode the parameters
as described in the [Client Message](#21-client-message) section.

### 5.3. Proxies
Before using a distributed object, the client SHOULD first create a proxy for the object. Do this by using the `CreateProxy`
request message.

To destroy a proxy, use the `DestroyProxy` request message.

#### 5.3.1. Proxy Creation

**Java Example:**
```java
HazelcastInstance client = HazelcastClient.newHazelcastClient();
IMap map = client.getMap("map-name");
```

**Python Example**
```python
client = HazelcastClient()
map = client.get_map("map-name")
```
Raw bytes for the create proxy request and response are shown below.

**Client Request**
```
// Initial frame
0x16 0x00 0x00 0x00 // Frame length
0x00 0xc0 // Flags
0x00 0x04 0x00 0x00 // Message type
0x30 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0xff 0xff 0xff 0xff // Partition ID
// Frame for the "map-name" string
0x0e 0x00 0x00 0x00 // Frame length
0x00 0x00 // Flags
0x6d 0x61 0x70 0x2d 0x6e 0x61 0x6d 0x65 // UTF-8 encoded data of the "map-name" string
// Frame for the name of the map service (which is "hz:impl:mapService")
0x18 0x00 0x00 0x00 // Frame length
0x00 0x20 // Flags
0x68 0x7a 0x3a 0x69 0x6d 0x70 0x6c 0x3a 0x6d 0x61 0x70 0x53 0x65 0x72 0x76 0x69 0x63 0x65 // UTF-8 encoded data of the "hz:impl:mapService" string
```

**Member Response**
```
// Initial frame
0x13 0x00 0x00 0x00 // Frame length
0x00 0xe0 // Flags
0x01 0x04 0x00 0x00 // Message type
0x30 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x00 // Backup acks count
```

For a request with a key, the client SHOULD send the request to the cluster member that houses the data for the key.
A client can do this by using the partition ID. For the `CreateProxy` request above, since the proxy creation is meant
to be sent to a random cluster member, partition ID is given as `-1`.

The response to a request message is always one of the following:
- Regular response message: The response is the message as listed in the protocol specification for the specific request message type.
- An error message: See the [Error Codes](#58-error-codes) section.

We give examples of operations on various data structures below.

#### 5.3.2. List Example

**Java Example**
```java
IList myList = client.getList("list"); // Create proxy
System.out.println(myList.get(3));
```

**Python Example**
```python
my_list = client.get_list("list") # Create proxy
print(my_list.get(3))
```
Raw bytes for get request and response are shown below.

**Client Request**
```
// Initial frame
0x1a 0x00 0x00 0x00 // Frame length
0x00 0xc0 // Flags
0x00 0x0f 0x05 0x00 // Message type
0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x7e 0x00 0x00 0x00 // Partition ID
0x03 0x00 0x00 0x00 // Item index: 3
// Frame for the list name
0x0a 0x00 0x00 0x00 // Frame length
0x00 0x20 // Flags
0x6c 0x69 0x73 0x74 // UTF-8 encoded data of the "list" string
```

**Member Response**
```
// Initial frame
0x13 0x00 0x00 0x00 // Frame length
0x00 0xc0 // Flags
0x01 0x0f 0x05 0x00 // Message type
0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x00 // Backup acks count
// Frame for the nullable Data frame
0x18 0x00 0x00 0x00
0x00 0x20
0x00 0x0c 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xff 0xff 0xff 0xf9 0x00 0x00 0x00 0x04 // Nullable Data for the returned value
```

#### 5.3.3. Fenced Lock Example
**Java Example**
```java
FencedLock myLock = client.getCPSubsystem().getLock("lock"); // Create proxy
myLock.lock();
```

Raw bytes for the lock request and response are shown below.

**Client Request**
```
// Initial frame
0x37 0x00 0x00 0x00 // Frame length
0x00 0xc0 // Flags
0x00 0x01 0x07 0x00 // Message type
0x07 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x11 0x00 0x00 0x00 // Partition ID
0x7b 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Session ID: 123
0x60 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Thread ID: 96
0x00 0x15 0xcd 0x5b 0x07 0x00 0x00 0x00 0x00 0xb1 0x68 0xde 0x3a 0x00 0x00 0x00 0x00 // Invocation UUID: UUID(123456789, 987654321)
// Frame for the RaftGroupID
// Begin frame for the RaftGroupId frame
0x06 0x00 0x00 0x00 // Frame length
0x00 0x10 // Flags
// Initial frame for the RaftGroupId
0x16 0x00 0x00 0x00 // Frame length
0x00 0x00 // Flags
0x36 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Seed: 54
0x40 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Id: 64
// String name parameter for the RaftGroupId
0x10 0x00 0x00 0x00 // Frame length
0x00 0x00 // Flags
0x72 0x61 0x66 0x74 0x2d 0x67 0x72 0x6f 0x75 0x70 // UTF-8 encoded name of the RaftGroup: "raft-group"
// End frame for the RaftGroupId
0x06 0x00 0x00 0x00
0x00 0x08
// String frame for the lock instance
0x0a 0x00 0x00 0x00 // Frame length
0x00 0x20 // Flags
0x6c 0x6f 0x63 0x6b // UTF-8 encoded name of the lock: "lock"
```

**Member Response**
```
// Initial frame
0x1b 0x00 0x00 0x00 // Frame length
0x00 0xe0 // Flags
0x01 0x01 0x07 0x00 // Message type
0x07 0x00 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x00 // Backup acks count
0x4e 0x61 0xbc 0x00 0x00 0x00 0x00 0x00 // Fence token: 12345678
```

#### 5.3.4. Map Example

**Java Example**
```java
String key = "key1";
int value = 54;
IMap myMap = client.getMap("map"); // Create proxy
myMap.put(key, value);
```
**Python Example**
```python
key = "key1"
value = 54
my_map = client.get_map("map") # Create proxy
my_map.put(key, value)
```

Raw bytes for the map put request and response are shown below.

**Client Request**
```
// Initial frame
0x26 0x00 0x00 0x00 // Frame length
0x00 0xc0 // Flags
0x00 0x01 0x01 0x00 // Message type
0x15 0x02 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x11 0x01 0x00 0x00 // Partition ID
0xf1 0xfb 0x90 0x00 0x00 0x00 0x00 0x00 // Thread ID: 654321
0x10 0x27 0x00 0x00 0x00 0x00 0x00 0x00 // TTL for the map: 10000
// String frame for the map name
0x09 0x00 0x00 0x00 // Frame length
0x00 0x00 // Flags
0x6d 0x61 0x70 // UTF-8 encoded name of the map: "map"
// Data frame for the key
0x16 0x00 0x00 0x00 // Frame length
0x00 0x00 // Flags
0x00 0x00 0x00 0x00 0xff 0xff 0xff 0xf5 0x00 0x00 0x00 0x04 0x6b 0x65 0x79 0x31 // Key data bytes
// Data frame for the value
0x12 0x00 0x00 0x00 // Frame length
0x00 0x00 // Flags
0x00 0x00 0x00 0x00 0xff 0xff 0xff 0xf9 0x00 0x00 0x00 0x36 // Value data bytes
```

**Member Response**
```
// Initial frame
0x13 0x00 0x00 0x00 // Frame length
0x00 0xc0 // Flags
0x01 0x01 0x01 0x00 // Message type
0x15 0x02 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x00 // Backup acks count
// Nullable response frame. Assuming there were no value associated with this key, response is set to null as below
0x06 0x00 0x00 0x00 // Frame length
0x00 0x40 // Flags
```

#### 5.3.5. Queue Example

**Java Example**
```java
IQueue myQueue = client.getQueue("queue"); // Create proxy
System.out.println(myQueue.size());
```

**Python Example**
```python
my_queue = client.get_queue("queue")
print(my_queue.size())
```

Raw bytes for the queue size request and response are shown below.

**Client Request**
```
// Initial frame
0x16 0x00 0x00 0x00 // Frame length
0x00 0xc0 // Flags
0x00 0x03 0x03 0x00 // Message type
0x12 0x33 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x01 0x01 0x00 0x00 // Partition ID
// String frame for the queue name
0x0b 0x00 0x00 0x00 // Frame length
0x00 0x20 // Flags
0x71 0x75 0x65 0x75 0x65 // UTF-8 encoded name of the queue: "queue"
```

**Member Response**
```
// Initial frame
0x17 0x00 0x00 0x00 // Frame length
0x00 0xe0 // Flags
0x01 0x03 0x03 0x00 // Message type
0x12 0x33 0x00 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x00 // Backup acks count
0x19 0x00 0x00 0x00 // Queue size: 25
```

#### 5.3.6. Set Example

**Java Example**
```java
ISet set = client.getSet("set"); // Create proxy
set.clear();
```

```python
set = client.get_set("set") # Create proxy
set.clear()
```

Raw bytes for the set clear request and response are shown below.

**Client Request**
```
// Initial frame
0x16 0x00 0x00 0x00 // Frame length
0x00 0xc0 // Flags
0x00 0x09 0x06 0x00 // Message type
0x0a 0x01 0xb5 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x03 0x02 0x00 0x00 // Partition ID
// String frame for the set name
0x09 0x00 0x00 0x00 // Frame length
0x00 0x20 // Flags
0x73 0x65 0x74 // UTF-8 encoded name of the set: "set"
```

**Member Response**
```
// Initial frame
0x13 0x00 0x00 0x00 // Frame length
0x00 0xe0 // Flags
0x01 0x09 0x06 0x00 // Message type
0x0a 0x01 0xb5 0x00 0x00 0x00 0x00 0x00 // Correlation ID
0x00 // Backup acks count
```

### 5.4. Multiple Responses to a Single Request
The client can listen for updates on a member or when specific actions are taken on the cluster. This is managed by the event listener mechanism.
The event messages have the `IS_EVENT_FLAG` bit is set in the initial frame and they use the same correlation ID as used in the original
registration request for all the subsequent event update messages. The registration message and possible event messages sent are
described in the `Event Message` section of the message descriptions.

### 5.5. Listeners
Listeners are mean to communicate multiple responses to a client. The client uses one of the listener registration messages to listen
for updates at the cluster. Listeners are specific to a data structure. For example, there is a specific listener for map entries and queue
items. To see how these listeners are explicitly encoded, see the relevant message in the
[Protocol Messages](#7-protocol-messages) section.

Because the same correlation ID is reused for every event response for a given request, the correlation ID MUST NOT be
reused from the event requests unless the client unregisters the listener.

One can send `RemoveListener` request message specific to the registration request to remove the listener that the client has
registered to.

### 5.6. Cluster View Listener
Cluster view consists of views of partition and member lists. The client gets the updates of these views as event responses
after registering a cluster view listener to one of the members of the cluster.

The partition list view tells the client which members handle which partition ID. The client can use this information
to send the related requests to the responsible member (for the request key if it exists) directly for processing.

The event response for the partition list view consists of the member-partition ownership information.

The other part of the cluster view is the member list view. This view is the list of members connected to the cluster. With this
information and the previous member list that the client has, member updates on the cluster such as member addition or removal
can be seen. This information is needed especially if the client operates as a smart client.

### 5.7. Timeouts and Retry
It is recommended that the client should be able to handle situations where the member may not be able to return the response
in an expected time interval. Even if the response to a specific message is not received, the user may or may not retry the
request. If the client retries the request, they SHOULD NOT use the same correlation ID.

If no message has been sent in the member's heartbeat time, the member will automatically disconnect from the client. To prevent
this from occurring, a client SHOULD submit a `Ping` request to the member periodically. A ping message is only sent from the
client to the member; the member does not perform any ping request.

### 5.8. Error Codes
The list of errors along with the error code and description is provided below. Note that there may be error messages with
an error code that is not listed in the table. The client can handle this situation differently based on the particular
implementation. (e.g. throw an unknown error code exception)

| Error Name | Error Code | Description |
| ---------- | ---------- | ----------- |
| ARRAY_INDEX_OUT_OF_BOUNDS | 1 | Thrown to indicate that an array has been accessed with an illegal index. The index is either negative or greater than or equal to the size of the array. |
| ARRAY_STORE | 2 | Thrown to indicate that an attempt has been made to store the wrong type of object into an array of objects. |
| AUTHENTICATION | 3 | The authentication failed. |
| CACHE | 4 | Thrown to indicate an exception has occurred in the Cache |
| CACHE_LOADER | 5 | An exception to indicate a problem has occurred executing a CacheLoader |
| CACHE_NOT_EXISTS | 6 | This exception class is thrown while creating CacheRecordStore instances but the cache config does not exist on the node to create the instance on. This can happen in either of two cases: the cache's config is not yet distributed to the node, or the cache has been already destroyed. For the first option, the caller can decide to just retry the operation a couple of times since distribution is executed in a asynchronous way. |
| CACHE_WRITER | 7 | An exception to indicate a problem has occurred executing a CacheWriter |
| CALLER_NOT_MEMBER | 8 | A retryable Hazelcast Exception that indicates that an operation was sent by a machine which isn't member in the cluster when the operation is executed. |
| CANCELLATION | 9 | Exception indicating that the result of a value-producing task, such as a FutureTask, cannot be retrieved because the task was cancelled. |
| CLASS_CAST | 10 | The class conversion (cast) failed. |
| CLASS_NOT_FOUND | 11 | The class does not exists in the loaded jars at the member. |
| CONCURRENT_MODIFICATION | 12 | The code is trying to modify a resource concurrently which is not allowed. |
| CONFIG_MISMATCH | 13 | Thrown when 2 nodes want to join, but their configuration doesn't match. |
| DISTRIBUTED_OBJECT_DESTROYED | 14 | The distributed object that you are trying to access is destroyed and does not exist. |
| EOF | 15 | End of file is reached (May be for a file or a socket) |
| ENTRY_PROCESSOR | 16 | An exception to indicate a problem occurred attempting to execute an EntryProcessor against an entry |
| EXECUTION | 17 | Thrown when attempting to retrieve the result of a task that aborted by throwing an exception. |
| HAZELCAST | 18 | General internal error of Hazelcast. |
| HAZELCAST_INSTANCE_NOT_ACTIVE | 19 | The Hazelcast member instance is not active, the server is possibly initialising. |
| HAZELCAST_OVERLOAD | 20 | Thrown when the system won't handle more load due to an overload. This exception is thrown when backpressure is enabled. |
| HAZELCAST_SERIALIZATION | 21 | Error during serialization/de-serialization of data. |
| IO | 22 | An IO error occurred. |
| ILLEGAL_ARGUMENT | 23 | Thrown to indicate that a method has been passed an illegal or inappropriate argument |
| ILLEGAL_ACCESS_EXCEPTION | 24 | An IllegalAccessException is thrown when an application tries to reflectively create an instance (other than an array), set or get a field, or invoke a method, but the currently executing method does not have access to the definition of the specified class, field, method or constructor |
| ILLEGAL_ACCESS_ERROR | 25 | Thrown if an application attempts to access or modify a field, or to call a method that it does not have access to |
| ILLEGAL_MONITOR_STATE | 26 | When an operation on a distributed object is being attempted by a thread which did not initially own the lock on the object. |
| ILLEGAL_STATE | 27 | Signals that a method has been invoked at an illegal or inappropriate time |
| ILLEGAL_THREAD_STATE | 28 | Thrown to indicate that a thread is not in an appropriate state for the requested operation. |
| INDEX_OUT_OF_BOUNDS | 29 | Thrown to indicate that an index of some sort (such as to a list) is out of range. |
| INTERRUPTED | 30 | Thrown when a thread is waiting, sleeping, or otherwise occupied, and the thread is interrupted, either before or during the activity |
| INVALID_ADDRESS | 31 | Thrown when given address is not valid. |
| INVALID_CONFIGURATION | 32 | An InvalidConfigurationException is thrown when there is an Invalid configuration. Invalid configuration can be a wrong Xml Config or logical config errors that are found at runtime. |
| MEMBER_LEFT | 33 | Thrown when a member left during an invocation or execution. |
| NEGATIVE_ARRAY_SIZE | 34 | The provided size of the array can not be negative but a negative number is provided. |
| NO_SUCH_ELEMENT | 35 | The requested element does not exist in the distributed object. |
| NOT_SERIALIZABLE | 36 | The object could not be serialized |
| NULL_POINTER | 37 | The server faced a null pointer exception during the operation. |
| OPERATION_TIMEOUT | 38 | Exception thrown when a blocking operation times out. |
| PARTITION_MIGRATING | 39 | Thrown when an operation is executed on a partition, but that partition is currently being moved around. |
| QUERY | 40 | Error during query. |
| QUERY_RESULT_SIZE_EXCEEDED | 41 | Thrown when a query exceeds a configurable result size limit. |
| SPLIT_BRAIN_PROTECTION | 42 | An exception thrown when the cluster size is below the defined threshold. |
| REACHED_MAX_SIZE | 43 | Exception thrown when a write-behind MapStore rejects to accept a new element. |
| REJECTED_EXECUTION | 44 | Exception thrown by an Executor when a task cannot be accepted for execution. |
| RESPONSE_ALREADY_SENT | 45 | There is some kind of system error causing a response to be send multiple times for some operation. |
| RETRYABLE_HAZELCAST | 46 | The operation request can be retried. |
| RETRYABLE_IO | 47 | Indicates that an operation can be retried. E.g. if map.get is send to a partition that is currently migrating, a subclass of this exception is thrown, so the caller can deal with it (e.g. sending the request to the new partition owner). |
| RUNTIME | 48 | Exceptions that can be thrown during the normal operation of the Java Virtual Machine |
| SECURITY | 49 | There is a security violation |
| SOCKET | 50 | There is an error in the underlying TCP protocol |
| STALE_SEQUENCE | 51 | Thrown when accessing an item in the Ringbuffer using a sequence that is smaller than the current head sequence. This means that the and old item is read, but it isn't available anymore in the ringbuffer. |
| TARGET_DISCONNECTED | 52 | Indicates that an operation is about to be sent to a non existing machine. |
| TARGET_NOT_MEMBER | 53 | Indicates operation is sent to a machine that isn't member of the cluster. |
| TIMEOUT | 54 | Exception thrown when a blocking operation times out |
| TOPIC_OVERLOAD | 55 | Thrown when a publisher wants to write to a topic, but there is not sufficient storage to deal with the event. This exception is only thrown in combination with the reliable topic. |
| TRANSACTION | 56 | Thrown when something goes wrong while dealing with transactions and transactional data-structures. |
| TRANSACTION_NOT_ACTIVE | 57 | Thrown when an a transactional operation is executed without an active transaction. |
| TRANSACTION_TIMED_OUT | 58 | Thrown when a transaction has timed out. |
| URI_SYNTAX | 59 | Thrown to indicate that a string could not be parsed as a URI reference |
| UTF_DATA_FORMAT | 60 | Signals that a malformed string in modified UTF-8 format has been read in a data input stream or by any class that implements the data input interface |
| UNSUPPORTED_OPERATION | 61 | The message type id for the operation request is not a recognised id. |
| WRONG_TARGET | 62 | An operation is executed on the wrong machine. |
| XA | 63 | An error occurred during an XA operation. |
| ACCESS_CONTROL | 64 | Indicates that a requested access to a system resource is denied. |
| LOGIN | 65 | Basic login exception. |
| UNSUPPORTED_CALLBACK | 66 | Signals that a CallbackHandler does not recognize a particular Callback. |
| NO_DATA_MEMBER | 67 | Thrown when there is no data member in the cluster to assign partitions. |
| REPLICATED_MAP_CANT_BE_CREATED | 68 | Thrown when replicated map create proxy request is invoked on a lite member. |
| MAX_MESSAGE_SIZE_EXCEEDED | 69 | Thrown when client message size exceeds Integer.MAX_VALUE. |
| WAN_REPLICATION_QUEUE_FULL | 70 | Thrown when the wan replication queues are full. |
| ASSERTION_ERROR | 71 | Thrown to indicate that an assertion has failed. |
| OUT_OF_MEMORY_ERROR | 72 | Thrown when the Java Virtual Machine cannot allocate an object because it is out of memory, and no more memory could be made available by the garbage collector. |
| STACK_OVERFLOW_ERROR | 73 | Thrown when a stack overflow occurs because an application recurses too deeply. |
| NATIVE_OUT_OF_MEMORY_ERROR | 74 | Thrown when Hazelcast cannot allocate required native memory. |
| SERVICE_NOT_FOUND | 75 | An exception that indicates that a requested client service doesn't exist. |
| STALE_TASK_ID | 76 | Thrown when retrieving the result of a task via DurableExecutorService if the result of the task is overwritten. This means the task is executed but the result isn't available anymore |
| DUPLICATE_TASK | 77 | thrown when a task's name is already used before for another (or the same, if re-attempted) schedule. |
| STALE_TASK | 78 | Exception thrown by the IScheduledFuture during any operation on a stale (=previously destroyed) task. |
| LOCAL_MEMBER_RESET | 79 | An exception provided to MemberLeftException as a cause when the local member is resetting itself |
| INDETERMINATE_OPERATION_STATE | 80 | Thrown when result of an invocation becomes indecisive. |
| FLAKE_ID_NODE_ID_OUT_OF_RANGE_EXCEPTION | 81 | Thrown from member if that member is not able to generate IDs using Flake ID generator because its node ID is too big. |
| TARGET_NOT_REPLICA_EXCEPTION | 82 | Exception that indicates that the receiver of a CRDT operation is not a CRDT replica. |
| MUTATION_DISALLOWED_EXCEPTION | 83 | Exception that indicates that the state found on this replica disallows mutation. |
| CONSISTENCY_LOST_EXCEPTION | 84 | Exception that indicates that the consistency guarantees provided by some service has been lost. The exact guarantees depend on the service. |
| SESSION_EXPIRED_EXCEPTION | 85 | Thrown when an operation is attached to a Raft session is no longer active |
| WAIT_KEY_CANCELLED_EXCEPTION | 86 | Thrown when a wait key is cancelled and means that the corresponding operation has not succeeded |
| LOCK_ACQUIRE_LIMIT_REACHED_EXCEPTION | 87 | Thrown when the current lock holder could not acquired the lock reentrantly because the configured lock acquire limit is reached. |
| LOCK_OWNERSHIP_LOST_EXCEPTION | 88 | Thrown when an endpoint (either a Hazelcast member or a client) interacts with a FencedLock instance after its CP session is closed in the underlying CP group and its lock ownership is cancelled. |
| CP_GROUP_DESTROYED_EXCEPTION | 89 | Thrown when a request is sent to a destroyed CP group. |
| CANNOT_REPLICATE_EXCEPTION | 90 | Thrown when an entry cannot be replicated |
| LEADER_DEMOTED_EXCEPTION | 91 | Thrown when an appended but not-committed entry is truncated by the new leader. |
| STALE_APPEND_REQUEST_EXCEPTION | 92 | Thrown when a Raft leader node appends an entry to its local Raft log, but demotes to the follower role before learning the commit status of the entry. |
| NOT_LEADER_EXCEPTION | 93 | Thrown when a leader-only request is received by a non-leader member. |
| VERSION_MISMATCH_EXCEPTION | 94 | Indicates that the version of a joining member is not compatible with the cluster version |
| NO_SUCH_METHOD_ERROR | 95 | Thrown if an application tries to call a specified method of a class (either static or instance), and that class no longer has a definition of that method. |
| NO_SUCH_METHOD_EXCEPTION | 96 | Thrown when a particular method cannot be found. |
| NO_SUCH_FIELD_ERROR | 97 | Thrown if an application tries to access or modify a specified field of an object, and that object no longer has that field. |
| NO_SUCH_FIELD_EXCEPTION | 98 | Signals that the class doesn't have a field of a specified name. |
| NO_CLASS_DEF_FOUND_ERROR | 99 | Thrown if the JVM or a ClassLoader instance tries to load in the definition of a class (as part of a normal method call or as part of creating a new instance using the new expression) and no definition of the class could be found. |

## 6. Miscellaneous

### 6.1. Smart Client and Unisocket Client
The client can work as a smart or as a unisocket client. In both cases, a client SHOULD calculate which partition ID
is responsible for the requests and put this information in the partition ID offset of the initial frame.

- **Smart Client:** A smart client sends the request directly to the cluster member that is responsible for the related key.
In order to do so, the client determines the address of the cluster member that handles the calculated partition ID.
The request message will be sent on this cluster member connection.

- **Unisocket Client:** The client sends the request to any cluster member that it is connected to, regardless of the key
for the request. The cluster member will in turn redirect the request to the correct member in the cluster that handles
the request for the provided key.

The biggest difference between the two types of clients is that a smart client must be connected to all the members and
must constantly update its partition tables so it knows which connection to use to submit a request. Both clients are compliant
with the protocol defined in this document.

### 6.2. Serialization
While mostly an implementation detail, serialization plays a crucial role in the protocol. In order for a client to execute
an operation on the member that involves data structure, such as putting some entry in a map or queue, the client must
be aware of how objects are serialized and deserialized so that the client can process the bytes it receives accordingly.
The member and client should use the same serialization versions in order to communicate. The version is negotiated in the
connection authentication phase. In general, one needs to use serialization to serialize byte-array type parameters in the messages as specified
in the [Protocol Messages](#7-protocol-messages) section. The following are examples of such objects that must be serialized
before being sent over the wire:

- Key
- Value
- Old value
- New value
- Callable (Executor Service)
- IFunction (Atomics)
- EntryProcessor (JCache)
- ExpiryPolicy (JCache)
- CacheConfig (JCache)
- ListenerConfig (JCache)
- Interceptor (Map)

A client may follow Hazelcast's native serialization or it may implement its own custom serialization solution. For more
information on how Hazelcast serializes its objects, see the official [Reference Manual](https://docs.hazelcast.org/docs/latest/manual/html-single/#serialization) serialization section.

For all byte-array parameters, the API users should implement the following, depending on the operation type:
- If the operation is such that no member side deserialization is needed for the parameter, then the user can just use
any serialization and there is no need for implementation on the member side.
- If the operation processing at the member requires deserialization of the byte-array parameter, then the user should
use a Java object implementing one of the Hazelcast serializations and may need to do some member side implementations
depending on the chosen serialization type. Furthermore, the serializer must be registered in the serialization configuration
of the member as described in the serialization section of the [Reference Manual](https://docs.hazelcast.org/docs/latest/manual/html-single/#serialization).

The client authentication request message contains the serialization version parameter. The client and the member decide the serialization
version to be used using this information. Hazelcast serialization versions will be matched to provide a compatible serialization.
There are two cases that can occur:
- The client may have a higher serialization version than the member. In that case, the client will auto configure
itself during authentication to match the member serialization version.
- The client may have a lower serialization version than the member. In that case, the member should be configured with
the system property to downgrade the member serialization version.

### 6.3. Security
Most of the security is configured on the member side in a Hazelcast cluster. A client must authenticate itself, which in turn
lets the member establish an endpoint for the client. The member can restrict what a client can and cannot access. The current protocol
does not provide explicit support for encryption. For more information, see the [Security](https://docs.hazelcast.org/docs/latest/manual/html-single/#security) chapter of the Hazelcast Reference Manual.

## 7. Protocol Messages
### 7.1. Custom Data Types Used In The Protocol
#### 7.1.1. Address
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| host | String | False | 2.0 |
| port | int | False | 2.0 |

#### 7.1.2. CacheEventData
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | False | 2.0 |
| cacheEventType | int | False | 2.0 |
| dataKey | Data | True | 2.0 |
| dataValue | Data | True | 2.0 |
| dataOldValue | Data | True | 2.0 |
| oldValueAvailable | boolean | False | 2.0 |

#### 7.1.3. CacheSimpleEntryListenerConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| oldValueRequired | boolean | False | 2.0 |
| synchronous | boolean | False | 2.0 |
| cacheEntryListenerFactory | String | True | 2.0 |
| cacheEntryEventFilterFactory | String | True | 2.0 |

#### 7.1.4. DistributedObjectInfo
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| serviceName | String | False | 2.0 |
| name | String | False | 2.0 |

#### 7.1.5. ErrorHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| errorCode | int | False | 2.0 |
| className | String | False | 2.0 |
| message | String | True | 2.0 |
| stackTraceElements | List of stackTraceElement | False | 2.0 |

#### 7.1.6. EventJournalConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| enabled | boolean | False | 2.0 |
| capacity | int | False | 2.0 |
| timeToLiveSeconds | int | False | 2.0 |

#### 7.1.7. EvictionConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| size | int | False | 2.0 |
| maxSizePolicy | String | False | 2.0 |
| evictionPolicy | String | False | 2.0 |
| comparatorClassName | String | True | 2.0 |
| comparator | Data | True | 2.0 |

#### 7.1.8. HotRestartConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| enabled | boolean | False | 2.0 |
| fsync | boolean | False | 2.0 |

#### 7.1.9. ListenerConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| listenerType | int | False | 2.0 |
| listenerImplementation | Data | True | 2.0 |
| className | String | True | 2.0 |
| includeValue | boolean | False | 2.0 |
| local | boolean | False | 2.0 |

#### 7.1.10. AttributeConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | False | 2.0 |
| extractorClassName | String | False | 2.0 |

#### 7.1.11. IndexConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | True | 2.0 |
| type | int | False | 2.0 |
| attributes | List of string | False | 2.0 |
| bitmapIndexOptions | BitmapIndexOptions | True | 2.0 |
| bTreeIndexConfig | BTreeIndexConfig | True | 2.5 |

#### 7.1.12. BitmapIndexOptions
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| uniqueKey | String | False | 2.0 |
| uniqueKeyTransformation | int | False | 2.0 |

#### 7.1.13. BTreeIndexConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| pageSize | Capacity | False | 2.5 |
| memoryTierConfig | MemoryTierConfig | False | 2.5 |

#### 7.1.14. MapStoreConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| enabled | boolean | False | 2.0 |
| writeCoalescing | boolean | False | 2.0 |
| writeDelaySeconds | int | False | 2.0 |
| writeBatchSize | int | False | 2.0 |
| className | String | True | 2.0 |
| implementation | Data | True | 2.0 |
| factoryClassName | String | True | 2.0 |
| factoryImplementation | Data | True | 2.0 |
| properties | Map of string to string | True | 2.0 |
| initialLoadMode | String | False | 2.0 |
| offload | boolean | False | 2.5 |

#### 7.1.15. MerkleTreeConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| enabled | boolean | False | 2.0 |
| depth | int | False | 2.0 |
| enabledSet | boolean | False | 2.3 |

#### 7.1.16. NearCacheConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | False | 2.0 |
| inMemoryFormat | String | False | 2.0 |
| serializeKeys | boolean | False | 2.0 |
| invalidateOnChange | boolean | False | 2.0 |
| timeToLiveSeconds | int | False | 2.0 |
| maxIdleSeconds | int | False | 2.0 |
| evictionConfigHolder | EvictionConfigHolder | False | 2.0 |
| cacheLocalEntries | boolean | False | 2.0 |
| localUpdatePolicy | String | False | 2.0 |
| preloaderConfig | NearCachePreloaderConfig | True | 2.0 |

#### 7.1.17. NearCachePreloaderConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| enabled | boolean | False | 2.0 |
| directory | String | False | 2.0 |
| storeInitialDelaySeconds | int | False | 2.0 |
| storeIntervalSeconds | int | False | 2.0 |

#### 7.1.18. PredicateConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| className | String | True | 2.0 |
| sql | String | True | 2.0 |
| implementation | Data | True | 2.0 |

#### 7.1.19. QueryCacheConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| batchSize | int | False | 2.0 |
| bufferSize | int | False | 2.0 |
| delaySeconds | int | False | 2.0 |
| includeValue | boolean | False | 2.0 |
| populate | boolean | False | 2.0 |
| coalesce | boolean | False | 2.0 |
| inMemoryFormat | String | False | 2.0 |
| name | String | False | 2.0 |
| predicateConfigHolder | PredicateConfigHolder | False | 2.0 |
| evictionConfigHolder | EvictionConfigHolder | False | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | 2.0 |
| indexConfigs | List of indexConfig | True | 2.0 |
| serializeKeys | boolean | False | 2.4 |

#### 7.1.20. QueryCacheEventData
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| dataKey | Data | True | 2.0 |
| dataNewValue | Data | True | 2.0 |
| sequence | long | False | 2.0 |
| eventType | int | False | 2.0 |
| partitionId | int | False | 2.0 |
| mapName | String | False | 2.7 |

#### 7.1.21. QueueStoreConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| className | String | True | 2.0 |
| factoryClassName | String | True | 2.0 |
| implementation | Data | True | 2.0 |
| factoryImplementation | Data | True | 2.0 |
| properties | Map of string to string | True | 2.0 |
| enabled | boolean | False | 2.0 |

#### 7.1.22. RaftGroupId
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | False | 2.0 |
| seed | long | False | 2.0 |
| id | long | False | 2.0 |

#### 7.1.23. RingbufferStoreConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| className | String | True | 2.0 |
| factoryClassName | String | True | 2.0 |
| implementation | Data | True | 2.0 |
| factoryImplementation | Data | True | 2.0 |
| properties | Map of string to string | True | 2.0 |
| enabled | boolean | False | 2.0 |

#### 7.1.24. ScheduledTaskHandler
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| uuid | UUID | True | 2.0 |
| partitionId | int | False | 2.0 |
| schedulerName | String | False | 2.0 |
| taskName | String | False | 2.0 |

#### 7.1.25. SimpleEntryView
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| key | Data | False | 2.0 |
| value | Data | False | 2.0 |
| cost | long | False | 2.0 |
| creationTime | long | False | 2.0 |
| expirationTime | long | False | 2.0 |
| hits | long | False | 2.0 |
| lastAccessTime | long | False | 2.0 |
| lastStoredTime | long | False | 2.0 |
| lastUpdateTime | long | False | 2.0 |
| version | long | False | 2.0 |
| ttl | long | False | 2.0 |
| maxIdle | long | False | 2.0 |

#### 7.1.26. StackTraceElement
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| className | String | False | 2.0 |
| methodName | String | False | 2.0 |
| fileName | String | True | 2.0 |
| lineNumber | int | False | 2.0 |

#### 7.1.27. DurationConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| durationAmount | long | False | 2.0 |
| timeUnit | int | False | 2.0 |

#### 7.1.28. TimedExpiryPolicyFactoryConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| expiryPolicyType | int | False | 2.0 |
| durationConfig | DurationConfig | False | 2.0 |

#### 7.1.29. WanReplicationRef
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | False | 2.0 |
| mergePolicyClassName | String | False | 2.0 |
| filters | List of string | True | 2.0 |
| republishingEnabled | boolean | False | 2.0 |

#### 7.1.30. Xid
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| formatId | int | False | 2.0 |
| globalTransactionId | byteArray | False | 2.0 |
| branchQualifier | byteArray | False | 2.0 |

#### 7.1.31. MergePolicyConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| policy | String | False | 2.0 |
| batchSize | int | False | 2.0 |

#### 7.1.32. CacheConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | False | 2.0 |
| managerPrefix | String | True | 2.0 |
| uriString | String | True | 2.0 |
| backupCount | int | False | 2.0 |
| asyncBackupCount | int | False | 2.0 |
| inMemoryFormat | String | False | 2.0 |
| evictionConfigHolder | EvictionConfigHolder | False | 2.0 |
| wanReplicationRef | WanReplicationRef | True | 2.0 |
| keyClassName | String | False | 2.0 |
| valueClassName | String | False | 2.0 |
| cacheLoaderFactory | Data | True | 2.0 |
| cacheWriterFactory | Data | True | 2.0 |
| expiryPolicyFactory | Data | False | 2.0 |
| readThrough | boolean | False | 2.0 |
| writeThrough | boolean | False | 2.0 |
| storeByValue | boolean | False | 2.0 |
| managementEnabled | boolean | False | 2.0 |
| statisticsEnabled | boolean | False | 2.0 |
| hotRestartConfig | HotRestartConfig | True | 2.0 |
| eventJournalConfig | EventJournalConfig | True | 2.0 |
| splitBrainProtectionName | String | True | 2.0 |
| listenerConfigurations | List of data | True | 2.0 |
| mergePolicyConfig | MergePolicyConfig | False | 2.0 |
| disablePerEntryInvalidationEvents | boolean | False | 2.0 |
| cachePartitionLostListenerConfigs | List of listenerConfigHolder | True | 2.0 |
| merkleTreeConfig | MerkleTreeConfig | True | 2.3 |
| dataPersistenceConfig | DataPersistenceConfig | False | 2.5 |
| userCodeNamespace | String | True | 2.7 |

#### 7.1.33. ClientBwListEntry
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| type | int | False | 2.0 |
| value | String | False | 2.0 |

#### 7.1.34. MemberInfo
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| address | Address | False | 2.0 |
| uuid | UUID | False | 2.0 |
| attributes | Map of string to string | False | 2.0 |
| liteMember | boolean | False | 2.0 |
| version | MemberVersion | False | 2.0 |
| addressMap | Map of endpointQualifier to address | False | 2.0.1 |

#### 7.1.35. EndpointQualifier
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| type | int | False | 2.0.1 |
| identifier | String | True | 2.0.1 |

#### 7.1.36. MemberVersion
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| major | byte | False | 2.0 |
| minor | byte | False | 2.0 |
| patch | byte | False | 2.0 |

#### 7.1.37. MCEvent
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| timestamp | long | False | 2.0 |
| type | int | False | 2.0 |
| dataJson | String | False | 2.0 |

#### 7.1.38. AnchorDataListHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| anchorPageList | List of integer | False | 2.0 |
| anchorDataList | Map of data to data | False | 2.0 |

#### 7.1.39. PagingPredicateHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| anchorDataListHolder | AnchorDataListHolder | False | 2.0 |
| predicateData | Data | True | 2.0 |
| comparatorData | Data | True | 2.0 |
| pageSize | int | False | 2.0 |
| page | int | False | 2.0 |
| iterationTypeId | byte | False | 2.0 |
| partitionKeyData | Data | True | 2.0 |
| partitionKeysData | List of data | True | 2.5 |

#### 7.1.40. SqlQueryId
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| memberIdHigh | long | False | 2.1 |
| memberIdLow | long | False | 2.1 |
| localIdHigh | long | False | 2.1 |
| localIdLow | long | False | 2.1 |

#### 7.1.41. SqlError
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| code | int | False | 2.1 |
| message | String | True | 2.1 |
| originatingMemberId | UUID | False | 2.1 |
| suggestion | String | True | 2.3 |
| causeStackTrace | String | True | 2.7 |

#### 7.1.42. SqlColumnMetadata
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | False | 2.1 |
| type | int | False | 2.1 |
| nullable | boolean | False | 2.2 |

#### 7.1.43. CPMember
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| uuid | UUID | False | 2.1 |
| address | Address | False | 2.1 |

#### 7.1.44. MigrationState
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| startTime | long | False | 2.2 |
| plannedMigrations | int | False | 2.2 |
| completedMigrations | int | False | 2.2 |
| totalElapsedTime | long | False | 2.2 |

#### 7.1.45. FieldDescriptor
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| fieldName | String | False | 2.3 |
| kind | int | False | 2.3 |

#### 7.1.46. Schema
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| typeName | String | False | 2.3 |
| fields | List of fieldDescriptor | False | 2.3 |

#### 7.1.47. HazelcastJsonValue
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| value | String | False | 2.4 |

#### 7.1.48. DataPersistenceConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| enabled | boolean | False | 2.5 |
| fsync | boolean | False | 2.5 |

#### 7.1.49. Capacity
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| value | long | False | 2.5 |
| unit | int | False | 2.5 |

#### 7.1.50. MemoryTierConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| capacity | Capacity | False | 2.5 |

#### 7.1.51. DiskTierConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| enabled | boolean | False | 2.5 |
| deviceName | String | False | 2.5 |

#### 7.1.52. TieredStoreConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| enabled | boolean | False | 2.5 |
| memoryTierConfig | MemoryTierConfig | False | 2.5 |
| diskTierConfig | DiskTierConfig | False | 2.5 |

#### 7.1.53. SqlSummary
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| query | String | False | 2.5 |
| unbounded | boolean | False | 2.5 |

#### 7.1.54. JobAndSqlSummary
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| lightJob | boolean | False | 2.5 |
| jobId | long | False | 2.5 |
| executionId | long | False | 2.5 |
| nameOrId | String | False | 2.5 |
| status | int | False | 2.5 |
| submissionTime | long | False | 2.5 |
| completionTime | long | False | 2.5 |
| failureText | String | True | 2.5 |
| sqlSummary | SqlSummary | True | 2.5 |
| suspensionCause | String | True | 2.6 |
| userCancelled | boolean | False | 2.6 |

#### 7.1.55. PartitioningAttributeConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| attributeName | String | False | 2.6 |

#### 7.1.56. WanConsumerConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| persistWanReplicatedData | boolean | False | 2.7 |
| className | String | True | 2.7 |
| implementation | Data | True | 2.7 |
| properties | Map of string to data | False | 2.7 |

#### 7.1.57. WanCustomPublisherConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| publisherId | String | True | 2.7 |
| className | String | True | 2.7 |
| implementation | Data | True | 2.7 |
| properties | Map of string to data | False | 2.7 |

#### 7.1.58. WanBatchPublisherConfigHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| publisherId | String | True | 2.7 |
| className | String | True | 2.7 |
| implementation | Data | True | 2.7 |
| properties | Map of string to data | False | 2.7 |
| clusterName | String | True | 2.7 |
| snapshotEnabled | boolean | False | 2.7 |
| initialPublisherState | byte | False | 2.7 |
| queueCapacity | int | False | 2.7 |
| batchSize | int | False | 2.7 |
| batchMaxDelayMillis | int | False | 2.7 |
| responseTimeoutMillis | int | False | 2.7 |
| queueFullBehavior | int | False | 2.7 |
| acknowledgeType | int | False | 2.7 |
| discoveryPeriodSeconds | int | False | 2.7 |
| maxTargetEndpoints | int | False | 2.7 |
| maxConcurrentInvocations | int | False | 2.7 |
| useEndpointPrivateAddress | boolean | False | 2.7 |
| idleMinParkNs | long | False | 2.7 |
| idleMaxParkNs | long | False | 2.7 |
| targetEndpoints | String | False | 2.7 |
| awsConfig | AwsConfig | False | 2.7 |
| gcpConfig | GcpConfig | False | 2.7 |
| azureConfig | AzureConfig | False | 2.7 |
| kubernetesConfig | KubernetesConfig | False | 2.7 |
| eurekaConfig | EurekaConfig | False | 2.7 |
| discoveryConfig | DiscoveryConfig | False | 2.7 |
| syncConfig | WanSyncConfig | False | 2.7 |
| endpoint | String | True | 2.7 |

#### 7.1.59. AwsConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| tag | String | False | 2.7 |
| enabled | boolean | False | 2.7 |
| usePublicIp | boolean | False | 2.7 |
| properties | Map of string to string | False | 2.7 |

#### 7.1.60. GcpConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| tag | String | False | 2.7 |
| enabled | boolean | False | 2.7 |
| usePublicIp | boolean | False | 2.7 |
| properties | Map of string to string | False | 2.7 |

#### 7.1.61. AzureConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| tag | String | False | 2.7 |
| enabled | boolean | False | 2.7 |
| usePublicIp | boolean | False | 2.7 |
| properties | Map of string to string | False | 2.7 |

#### 7.1.62. KubernetesConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| tag | String | False | 2.7 |
| enabled | boolean | False | 2.7 |
| usePublicIp | boolean | False | 2.7 |
| properties | Map of string to string | False | 2.7 |

#### 7.1.63. EurekaConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| tag | String | False | 2.7 |
| enabled | boolean | False | 2.7 |
| usePublicIp | boolean | False | 2.7 |
| properties | Map of string to string | False | 2.7 |

#### 7.1.64. DiscoveryStrategyConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| className | String | False | 2.7 |
| properties | Map of string to data | False | 2.7 |

#### 7.1.65. DiscoveryConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| discoveryStrategyConfigs | List of discoveryStrategyConfig | False | 2.7 |
| discoveryServiceProvider | Data | False | 2.7 |
| nodeFilter | Data | False | 2.7 |
| nodeFilterClass | String | False | 2.7 |

#### 7.1.66. WanSyncConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| consistencyCheckStrategy | byte | False | 2.7 |

#### 7.1.67. ReplicatedMapEntryViewHolder
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| key | Data | False | 2.7 |
| value | Data | False | 2.7 |
| creationTime | long | False | 2.7 |
| hits | long | False | 2.7 |
| lastAccessTime | long | False | 2.7 |
| lastUpdateTime | long | False | 2.7 |
| ttlMillis | long | False | 2.7 |

#### 7.1.68. ResourceDefinition
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| id | String | False | 2.7 |
| resourceType | int | False | 2.7 |
| payload | byteArray | True | 2.7 |
| resourceUrl | String | True | 2.7 |

#### 7.1.69. VectorIndexConfig
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | True | 2.8 |
| metric | int | False | 2.8 |
| dimension | int | False | 2.8 |
| maxDegree | int | False | 2.8 |
| efConstruction | int | False | 2.8 |
| useDeduplication | boolean | False | 2.8 |

#### 7.1.70. VectorPair
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| name | String | False | 2.8 |
| type | byte | False | 2.8 |
| vector | floatArray | True | 2.8 |

#### 7.1.71. VectorDocument
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| value | Data | False | 2.8 |
| vectors | List of vectorPair | False | 2.8 |

#### 7.1.72. VectorSearchOptions
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| includeValue | boolean | False | 2.8 |
| includeVectors | boolean | False | 2.8 |
| limit | int | False | 2.8 |
| hints | Map of string to string | True | 2.8 |

#### 7.1.73. VectorSearchResult
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| key | Data | False | 2.8 |
| value | Data | True | 2.8 |
| score | float | False | 2.8 |
| vectors | List of vectorPair | True | 2.8 |

#### 7.1.74. Version
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| major | byte | False | 2.8 |
| minor | byte | False | 2.8 |

#### 7.1.75. RaftGroupInfo
**Parameters**

| Name | Type | Nullable | Available Since |
| ---- | ---- | -------- | --------------- |
| groupId | RaftGroupId | False | 2.8 |
| leader | CPMember | False | 2.8 |
| followers | List of cPMember | False | 2.8 |


### 7.2. Client
**Service id:** 0

#### 7.2.1. Client.Authentication
```
Makes an authentication request to the cluster.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| clusterName | String | False | Cluster name that client will connect to. | 2.0 |
| username | String | True | Name of the user for authentication. Used in case Client Identity Config, otherwise it should be passed null. | 2.0 |
| password | String | True | Password for the user. Used in case Client Identity Config, otherwise it should be passed null. | 2.0 |
| uuid | UUID | True | Unique string identifying the connected client uniquely. | 2.0 |
| clientType | String | False | The type of the client. E.g. JAVA, CPP, CSHARP, etc. | 2.0 |
| serializationVersion | byte | False | client side supported version to inform server side | 2.0 |
| clientHazelcastVersion | String | False | The Hazelcast version of the client. (e.g. 3.7.2) | 2.0 |
| clientName | String | False | the name of the client instance | 2.0 |
| labels | List of string | False | User defined labels of the client instance | 2.0 |
| routingMode | byte | False | Identifies the routing mode of the client. It can be UNISOCKET(0), SMART(1) or SUBSET(2). | 2.8 |
| cpDirectToLeaderRouting | boolean | False | The client's CP direct-to-leader routing setting (enabled or disabled) | 2.8 |

#### Response Message
**Message Type:** 0x000101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| status | byte | False | A byte that represents the authentication status. It can be AUTHENTICATED(0), CREDENTIALS_FAILED(1), SERIALIZATION_VERSION_MISMATCH(2) or NOT_ALLOWED_IN_CLUSTER(3). | 2.0 |
| address | Address | True | Address of the Hazelcast member which sends the authentication response. | 2.0 |
| memberUuid | UUID | True | UUID of the Hazelcast member which sends the authentication response. | 2.0 |
| serializationVersion | byte | False | client side supported version to inform server side | 2.0 |
| serverHazelcastVersion | String | False | Version of the Hazelcast member which sends the authentication response. | 2.0 |
| partitionCount | int | False | Partition count of the cluster. | 2.0 |
| clusterId | UUID | False | UUID of the cluster that the client authenticated. | 2.0 |
| failoverSupported | boolean | False | Returns true if server supports clients with failover feature. | 2.0 |
| tpcPorts | List of integer | True | Returns the list of TPC ports or null if TPC is disabled. | 2.7 |
| tpcToken | byteArray | True | Returns the token to use while authenticating TPC channels  or null if TPC is disabled. | 2.7 |
| memberListVersion | int | False | Incremental member list version. -1 if no member list is available. | 2.7 |
| memberInfos | List of memberInfo | False | List of member infos  at the cluster associated with the given version | 2.7 |
| partitionListVersion | int | False | Incremental state version of the partition table. -1 if no partition table is available. | 2.7 |
| partitions | Map of uUID to list_Integer | False | The partition table. In each entry, it has uuid of the member and list of partitions belonging to that member | 2.7 |
| keyValuePairs | Map of string to string | False | Server/Member metadata represented as in key value pairs | 2.8 |

#### 7.2.2. Client.AuthenticationCustom
```
Makes an authentication request to the cluster using custom credentials.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| clusterName | String | False | Cluster name that client will connect to. | 2.0 |
| credentials | byteArray | False | Secret byte array for authentication. | 2.0 |
| uuid | UUID | True | Unique string identifying the connected client uniquely. | 2.0 |
| clientType | String | False | The type of the client. E.g. JAVA, CPP, CSHARP, etc. | 2.0 |
| serializationVersion | byte | False | client side supported version to inform server side | 2.0 |
| clientHazelcastVersion | String | False | The Hazelcast version of the client. (e.g. 3.7.2) | 2.0 |
| clientName | String | False | the name of the client instance | 2.0 |
| labels | List of string | False | User defined labels of the client instance | 2.0 |
| routingMode | byte | False | Identifies the routing mode of the client. It can be UNISCOKET(0), SMART(1) or SUBSET(2). | 2.8 |
| cpDirectToLeaderRouting | boolean | False | The client's CP direct-to-leader routing setting (enabled or disabled) | 2.8 |

#### Response Message
**Message Type:** 0x000201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| status | byte | False | A byte that represents the authentication status. It can be AUTHENTICATED(0), CREDENTIALS_FAILED(1), SERIALIZATION_VERSION_MISMATCH(2) or NOT_ALLOWED_IN_CLUSTER(3). | 2.0 |
| address | Address | True | Address of the Hazelcast member which sends the authentication response. | 2.0 |
| memberUuid | UUID | True | UUID of the Hazelcast member which sends the authentication response. | 2.0 |
| serializationVersion | byte | False | client side supported version to inform server side | 2.0 |
| serverHazelcastVersion | String | False | Version of the Hazelcast member which sends the authentication response. | 2.0 |
| partitionCount | int | False | Partition count of the cluster. | 2.0 |
| clusterId | UUID | False | The cluster id of the cluster. | 2.0 |
| failoverSupported | boolean | False | Returns true if server supports clients with failover feature. | 2.0 |
| tpcPorts | List of integer | True | Returns the list of TPC ports or null if TPC is disabled. | 2.7 |
| tpcToken | byteArray | True | Returns the token to use while authenticating TPC channels  or null if TPC is disabled. | 2.7 |
| memberListVersion | int | False | Incremental member list version | 2.7 |
| memberInfos | List of memberInfo | True | List of member infos  at the cluster associated with the given version | 2.7 |
| partitionListVersion | int | False | Incremental state version of the partition table | 2.7 |
| partitions | Map of uUID to list_Integer | True | The partition table. In each entry, it has uuid of the member and list of partitions belonging to that member | 2.7 |
| keyValuePairs | Map of string to string | False | Server/Member metadata represented as in key value pairs | 2.8 |

#### 7.2.3. Client.AddClusterViewListener
```
Adds a cluster view listener to a connection.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000300

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0x000301

Header only response message, no message body exist.

#### Event Message

##### MembersView
**Message Type:** 0x000303

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| version | int | False | Incremental member list version | 2.0 |
| memberInfos | List of memberInfo | False | List of member infos  at the cluster associated with the given version params: | 2.0 |

##### PartitionsView
**Message Type:** 0x000304

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| version | int | False | Incremental state version of the partition table | 2.0 |
| partitions | Map of uUID to list_Integer | False | The partition table. In each entry, it has uuid of the member and list of partitions belonging to that member | 2.0 |

##### MemberGroupsView
**Message Type:** 0x000305

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| version | int | False | Holds the state of member-groups and member-list-version | 2.8 |
| memberGroups | List of list_UUID | False | Grouped members by their UUID. Grouping is done based on RoutingStrategy. | 2.8 |

##### ClusterVersion
**Message Type:** 0x000306

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| version | Version | False | The cluster version. | 2.8 |

#### 7.2.4. Client.CreateProxy
```
Creates a cluster-wide proxy with the given name and service.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | The distributed object name for which the proxy is being created for. | 2.0 |
| serviceName | String | False | The name of the service. Possible service names are: "hz:impl:listService" "hz:impl:queueService" "hz:impl:setService" "hz:impl:idGeneratorService" "hz:impl:executorService" "hz:impl:mapService" "hz:impl:multiMapService" "hz:impl:splitBrainProtectionService" "hz:impl:replicatedMapService" "hz:impl:ringbufferService" "hz:core:proxyService" "hz:impl:reliableTopicService" "hz:impl:topicService" "hz:core:txManagerService" "hz:impl:xaService" | 2.0 |

#### Response Message
**Message Type:** 0x000401

Header only response message, no message body exist.

#### 7.2.5. Client.DestroyProxy
```
Destroys the proxy given by its name cluster-wide. Also, clears and releases all resources of this proxy.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | The distributed object name for which the proxy is being destroyed for. | 2.0 |
| serviceName | String | False | The name of the service. Possible service names are: "hz:impl:listService" "hz:impl:queueService" "hz:impl:setService" "hz:impl:idGeneratorService" "hz:impl:executorService" "hz:impl:mapService" "hz:impl:multiMapService" "hz:impl:splitBrainProtectionService" "hz:impl:replicatedMapService" "hz:impl:ringbufferService" "hz:core:proxyService" "hz:impl:reliableTopicService" "hz:impl:topicService" "hz:core:txManagerService" "hz:impl:xaService" | 2.0 |

#### Response Message
**Message Type:** 0x000501

Header only response message, no message body exist.

#### 7.2.6. Client.AddPartitionLostListener
```
Adds a partition lost listener to the cluster.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| localOnly | boolean | False | if true only node that has the partition sends the request, if false sends all partition lost events. | 2.0 |

#### Response Message
**Message Type:** 0x000601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | The listener registration id. | 2.0 |

#### Event Message

##### PartitionLost
**Message Type:** 0x000603

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| partitionId | int | False | Id of the lost partition. | 2.0 |
| lostBackupCount | int | False | The number of lost backups for the partition. 0: the owner, 1: first backup, 2: second backup... | 2.0 |
| source | UUID | True | UUID of the node that dispatches the event | 2.0 |

#### 7.2.7. Client.RemovePartitionLostListener
```
Removes the specified partition lost listener. If there is no such listener added before, this call does no change
in the cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| registrationId | UUID | False | The id assigned during the listener registration. | 2.0 |

#### Response Message
**Message Type:** 0x000701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the listener existed and removed, false otherwise. | 2.0 |

#### 7.2.8. Client.GetDistributedObjects
```
Gets the list of distributed objects in the cluster.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000800

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0x000801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of distributedObjectInfo | False | An array of distributed object info in the cluster. | 2.0 |

#### 7.2.9. Client.AddDistributedObjectListener
```
Adds a distributed object listener to the cluster. This listener will be notified
when a distributed object is created or destroyed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| localOnly | boolean | False | If set to true, the server adds the listener only to itself, otherwise the listener is is added for all members in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x000901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | The registration id for the distributed object listener. | 2.0 |

#### Event Message

##### DistributedObject
**Message Type:** 0x000903

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the distributed object. | 2.0 |
| serviceName | String | False | Service name of the distributed object. | 2.0 |
| eventType | String | False | Type of the event. It is either CREATED or DESTROYED. | 2.0 |
| source | UUID | False | The UUID (client or member) of the source of this proxy event. | 2.0 |

#### 7.2.10. Client.RemoveDistributedObjectListener
```
Removes the specified distributed object listener. If there is no such listener added before, this call does no
change in the cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| registrationId | UUID | False | The id assigned during the registration. | 2.0 |

#### Response Message
**Message Type:** 0x000a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the listener existed and removed, false otherwise. | 2.0 |

#### 7.2.11. Client.Ping
```
Sends a ping to the given connection.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000b00

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0x000b01

Header only response message, no message body exist.

#### 7.2.12. Client.Statistics
```
The statistics is composed of three parameters.

The first paramteter is the timestamp taken when the statistics collected.

The second parameter, the clientAttribute is a String that is composed of key=value pairs separated by ','. The
following characters ('=' '.' ',' '\') should be escaped.

Please note that if any client implementation can not provide the value for statistics, the corresponding key, value
pair will not be presented in the statistics string. Only the ones, that the client can provide will be added.

The third parameter, metrics is a compressed byte array containing all metrics recorded by the client.

The metrics are composed of the following fields:
  - string:                 prefix
  - string:                 metric
  - string:                 discriminator
  - string:                 discriminatorValue
  - enum:                   unit [BYTES,MS,PERCENT,COUNT,BOOLEAN,ENUM]
  - set of enum:            excluded targets [MANAGEMENT_CENTER,JMX,DIAGNOSTICS]
  - set of <string,string>: tags associated with the metric

The used compression algorithm is the same that is used inside the IMDG clients and members for storing the metrics blob
in-memory. The algorithm uses a dictionary based delta compression further deflated by using ZLIB compression.

The byte array has the following layout:

+---------------------------------+--------------------+
| Compressor version              |   2 bytes (short)  |
+---------------------------------+--------------------+
| Size of dictionary blob         |   4 bytes (int)    |
+---------------------------------+--------------------+
| ZLIB compressed dictionary blob |   variable size    |
+---------------------------------+--------------------+
| Number of metrics in the blob   |   4 bytes (int)    |
+---------------------------------+--------------------+
| ZLIB compressed metrics blob    |   variable size    |
+---------------------------------+--------------------+

==========
THE HEADER
==========

Compressor version:      the version currently in use is 1.
Size of dictionary blob: the size of the ZLIB compressed blob as it is constructed as follows.

===================
THE DICTIONARY BLOB
===================

The dictionary is built from the string fields of the metric and assigns an int dictionary id to every string in the metrics
in the blob. The dictionary is serialized to the dictionary blob sorted by the strings using the following layout.

+------------------------------------------------+--------------------+
| Number of dictionary entries                   |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| Dictionary id                                  |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| Number of chars shared with previous entry     |   1 unsigned byte  |
+------------------------------------------------+--------------------+
| Number of chars not shared with previous entry |   1 unsigned byte  |
+------------------------------------------------+--------------------+
| The different characters                       |   variable size    |
+------------------------------------------------+--------------------+
| Dictionary id                                  |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| ...                                            |   ...              |
+------------------------------------------------+--------------------+

Let's say we have the following dictionary:
  - <42,"gc.minorCount">
  - <43,"gc.minorTime">

It is then serialized as follows:
+------------------------------------------------+--------------------+
| 2 (size of the dictionary)                     |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| 42                                             |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| 0                                              |   1 unsigned byte  |
+------------------------------------------------+--------------------+
| 13                                             |   1 unsigned byte  |
+------------------------------------------------+--------------------+
| "gc.minorCount"                                |   13 bytes         |
+------------------------------------------------+--------------------+
| 43                                             |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| 8                                              |   1 unsigned byte  |
+------------------------------------------------+--------------------+
| 4                                              |   1 unsigned byte  |
+------------------------------------------------+--------------------+
| "Time"                                         |   13 bytes         |
+------------------------------------------------+--------------------+

The dictionary blob constructed this way is then gets ZLIB compressed.

===============
THE METRIC BLOB
===============

The compressed dictionary blob is followed by the number of metrics
(int) present in the metrics blob.

The number of metrics is followed by the compressed metrics blob with
the following layout:

+------------------------------------------------+--------------------+
| Metrics mask                                   |   1 byte           |
+------------------------------------------------+--------------------+
| (*) Dictionary id of prefix                    |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| (*) Dictionary id of metric                    |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| (*) Dictionary id of discriminator             |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| (*) Dictionary id of discriminatorValue        |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| (*) Enum ordinal of the unit                   |   1 byte           |
+------------------------------------------------+--------------------+
| (*) Excluded targets bitset                    |   1 byte           |
+------------------------------------------------+--------------------+
| (*) Number of tags                             |   1 unsigned byte  |
+------------------------------------------------+--------------------+
| (**) Dictionary id of the tag 1                |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| (**) Dictionary id of the value of tag 1       |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| (**) Dictionary id of the tag 2                |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| (**) Dictionary id of the value of tag 2       |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| ...                                            |   ...              |
+------------------------------------------------+--------------------+
| Metrics mask                                   |   1 byte           |
+------------------------------------------------+--------------------+
| (*) Dictionary id of prefix                    |   4 bytes (int)    |
+------------------------------------------------+--------------------+
| ...                                            |   ...              |
+------------------------------------------------+--------------------+

The metrics mask shows which fields are the same in the current and the
previous metric. The following masks are used to construct the metrics
mask.

MASK_PREFIX              = 0b00000001;
MASK_METRIC              = 0b00000010;
MASK_DISCRIMINATOR       = 0b00000100;
MASK_DISCRIMINATOR_VALUE = 0b00001000;
MASK_UNIT                = 0b00010000;
MASK_EXCLUDED_TARGETS    = 0b00100000;
MASK_TAG_COUNT           = 0b01000000;

If a bit representing a field is set, the given field marked above with (*)
is not written to blob and the last value for that field should be taken
during deserialization.

Since the number of tags are not limited, all tags and their values
marked with (**) are written even if the tag set is the same as in the
previous metric.

The metrics blob constructed this way is then gets ZLIB compressed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| timestamp | long | False | The timestamp taken during statistics collection. | 2.0 |
| clientAttributes | String | False | The key=value pairs separated by the ',' character. | 2.0 |
| metricsBlob | byteArray | False | Compressed byte array containing all metrics collected by the client. | 2.0 |

#### Response Message
**Message Type:** 0x000c01

Header only response message, no message body exist.

#### 7.2.13. Client.DeployClasses
```
Deploys the list of classes to cluster
Each item is a Map.Entry<String, byte[]> in the list.
key of entry is full class name, and byte[] is the class definition.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| classDefinitions | Map of string to byteArray | False | list of class definitions | 2.0 |

#### Response Message
**Message Type:** 0x000d01

Header only response message, no message body exist.

#### 7.2.14. Client.CreateProxies
```
Proxies will be created on all cluster members.
If the member is  a lite member, a replicated map will not be created.
Any proxy creation failure is logged on the server side.
Exceptions related to a proxy creation failure is not send to the client.
A proxy creation failure does not cancel this operation, all proxies will be attempted to be created.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| proxies | Map of string to string | False | proxies that will be created Each entry's key is distributed object name. Each entry's value is service name. For possible service names see createProxy message. | 2.0 |

#### Response Message
**Message Type:** 0x000e01

Header only response message, no message body exist.

#### 7.2.15. Client.LocalBackupListener
```
Adds listener for backup acks

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x000f00

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0x000f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Returns the registration id for the listener. | 2.0 |

#### Event Message

##### backup
**Message Type:** 0x000f03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| sourceInvocationCorrelationId | long | False | correlation id of the invocation that backup acks belong to | 2.0 |

#### 7.2.16. Client.TriggerPartitionAssignment
```
Triggers partition assignment manually on the cluster.
Note that Partition based operations triggers this automatically

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x001000

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0x001001

Header only response message, no message body exist.

#### 7.2.17. Client.AddMigrationListener
```
Adds a migration listener to the cluster.

```

**Available since:** 2.2

#### Request Message
**Message Type:** 0x001100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| localOnly | boolean | False | If set to true, the server adds the listener only to itself, otherwise the listener is added for all members in the cluster. | 2.2 |

#### Response Message
**Message Type:** 0x001101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | The listener registration id. | 2.2 |

#### Event Message

##### Migration
**Message Type:** 0x001103

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| migrationState | MigrationState | False | Migration state. | 2.2 |
| type | int | False | Type of the event. It is either MIGRATION_STARTED(0) or MIGRATION_FINISHED(1). | 2.2 |

##### ReplicaMigration
**Message Type:** 0x001104

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| migrationState | MigrationState | False | The progress information of the overall migration. | 2.2 |
| partitionId | int | False | The partition ID that the event is dispatched for. | 2.2 |
| replicaIndex | int | False | The index of the partition replica. | 2.2 |
| sourceUuid | UUID | True | The id of old owner of the migrating partition replica. | 2.2 |
| destUuid | UUID | True | The id of new owner of the migrating partition replica. | 2.2 |
| success | boolean | False | The result of the migration: completed or failed. | 2.2 |
| elapsedTime | long | False | The elapsed the time of this migration in milliseconds. | 2.2 |

#### 7.2.18. Client.RemoveMigrationListener
```
Removes the specified migration listener.

```

**Available since:** 2.2

#### Request Message
**Message Type:** 0x001200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| registrationId | UUID | False | The id assigned during the listener registration. | 2.2 |

#### Response Message
**Message Type:** 0x001201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the listener existed and was removed, false otherwise. | 2.2 |

#### 7.2.19. Client.SendSchema
```
Sends a schema to cluster

```

**Available since:** 2.5

#### Request Message
**Message Type:** 0x001300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schema | Schema | False | schema to be send to the cluster | 2.5 |

#### Response Message
**Message Type:** 0x001301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| replicatedMembers | Set_UUID | False | UUIDs of the members that the schema is replicated | 2.5 |

#### 7.2.20. Client.FetchSchema
```
Fetches a schema from the cluster with the given schemaId

```

**Available since:** 2.5

#### Request Message
**Message Type:** 0x001400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schemaId | long | False | Id of the schema to be fetched | 2.5 |

#### Response Message
**Message Type:** 0x001401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schema | Schema | True | schema with the given schema id fetched from the cluster | 2.5 |

#### 7.2.21. Client.SendAllSchemas
```
Sends all the schemas to the cluster

```

**Available since:** 2.5

#### Request Message
**Message Type:** 0x001500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schemas | List of schema | False | list of schemas | 2.5 |

#### Response Message
**Message Type:** 0x001501

Header only response message, no message body exist.

#### 7.2.22. Client.TpcAuthentication
```
Makes an authentication request to TPC channels.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x001600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| uuid | UUID | False | UUID of the client. | 2.7 |
| token | byteArray | False | Authentication token bytes for the TPC channels | 2.7 |

#### Response Message
**Message Type:** 0x001601

Header only response message, no message body exist.

#### 7.2.23. Client.AddCPGroupViewListener
```
Adds a CP Group view listener to a connection.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x001700

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0x001701

Header only response message, no message body exist.

#### Event Message

##### GroupsView
**Message Type:** 0x001703

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| version | long | False | The version number for this group view | 2.8 |
| groupsInfo | List of raftGroupInfo | False | List of RaftGroupInfo objects containing group IDs, leader, and follower information | 2.8 |
| cpToApUuids | Map of uUID to uUID | False | Mapping of CP UUIDs to AP UUIDs, for use on the client | 2.8 |

### 7.3. Map
**Service id:** 1

#### 7.3.1. Map.Put
```
Puts an entry into this map with a given ttl (time to live) value.Entry will expire and get evicted after the ttl
If ttl is 0, then the entry lives forever.This method returns a clone of the previous value, not the original
(identically equal) value previously put into the map.Time resolution for TTL is seconds. The given TTL value is
rounded to the next closest second value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010100

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | Value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x010101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | old value of the entry | 2.0 |

#### 7.3.2. Map.Get
```
This method returns a clone of the original value, so modifying the returned value does not change the actual
value in the map. You should put the modified value back to make changes visible to all nodes.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010200

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x010201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The value for the key if exists | 2.0 |

#### 7.3.3. Map.Remove
```
Removes the mapping for a key from this map if it is present (optional operation).
Returns the value to which this map previously associated the key, or null if the map contained no mapping for the key.
If this map permits null values, then a return value of null does not necessarily indicate that the map contained no mapping for the key; it's also
possible that the map explicitly mapped the key to null. The map will not contain a mapping for the specified key once the
call returns.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010300

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x010301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | Clone of the removed value, not the original (identically equal) value previously put into the map. | 2.0 |

#### 7.3.4. Map.Replace
```
Replaces the entry for a key only if currently mapped to a given value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010400

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | New value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x010401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | Clone of the previous value, not the original (identically equal) value previously put into the map. | 2.0 |

#### 7.3.5. Map.ReplaceIfSame
```
Replaces the the entry for a key only if existing values equal to the testValue

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010500

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| testValue | Data | False | Test the existing value against this value to find if equal to this value. | 2.0 |
| value | Data | False | New value for the map entry. Only replace with this value if existing value is equal to the testValue. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x010501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if value is replaced with new one, false otherwise | 2.0 |

#### 7.3.6. Map.ContainsKey
```
Returns true if this map contains a mapping for the specified key.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010600

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x010601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if the key exists, otherwise returns false. | 2.0 |

#### 7.3.7. Map.ContainsValue
```
Returns true if this map maps one or more keys to the specified value.This operation will probably require time
linear in the map size for most implementations of the Map interface.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| value | Data | False | Value to check if exists in the map. | 2.0 |

#### Response Message
**Message Type:** 0x010701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if the value exists, otherwise returns false. | 2.0 |

#### 7.3.8. Map.RemoveIfSame
```
Removes the mapping for a key from this map if existing value equal to the this value

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010800

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | Test the existing value against this value to find if equal to this value. Only remove the entry from the map if the value is equal to this value. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x010801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if the key exists and removed, otherwise returns false. | 2.0 |

#### 7.3.9. Map.Delete
```
Removes the mapping for a key from this map if it is present.Unlike remove(Object), this operation does not return
the removed value, which avoids the serialization cost of the returned value.If the removed value will not be used,
a delete operation is preferred over a remove operation for better performance. The map will not contain a mapping
for the specified key once the call returns.
This method breaks the contract of EntryListener. When an entry is removed by delete(), it fires an EntryEvent
with a null oldValue. Also, a listener with predicates will have null values, so only keys can be queried via predicates

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010900

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x010901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if the key exists and removed, otherwise returns false. | 2.7 |

#### 7.3.10. Map.Flush
```
If this map has a MapStore, this method flushes all the local dirty entries by calling MapStore.storeAll()
and/or MapStore.deleteAll().

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |

#### Response Message
**Message Type:** 0x010a01

Header only response message, no message body exist.

#### 7.3.11. Map.TryRemove
```
Tries to remove the entry with the given key from this map within the specified timeout value.
If the key is already locked by another thread and/or member, then this operation will wait the timeout
amount for acquiring the lock.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010b00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| timeout | long | False | maximum time in milliseconds to wait for acquiring the lock for the key. | 2.0 |

#### Response Message
**Message Type:** 0x010b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if successful, otherwise returns false | 2.0 |

#### 7.3.12. Map.TryPut
```
Tries to put the given key and value into this map within a specified timeout value. If this method returns false,
it means that the caller thread could not acquire the lock for the key within the timeout duration,
thus the put operation is not successful.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010c00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | New value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| timeout | long | False | maximum time in milliseconds to wait for acquiring the lock for the key. | 2.0 |

#### Response Message
**Message Type:** 0x010c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if successful, otherwise returns false | 2.0 |

#### 7.3.13. Map.PutTransient
```
Same as put except that MapStore, if defined, will not be called to store/persist the entry.
If ttl is 0, then the entry lives forever.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010d00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | New value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x010d01

Header only response message, no message body exist.

#### 7.3.14. Map.PutIfAbsent
```
Puts an entry into this map with a given ttl (time to live) value if the specified key is not already associated
with a value. Entry will expire and get evicted after the ttl.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010e00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | New value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x010e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | returns a clone of the previous value, not the original (identically equal) value previously put into the map. | 2.0 |

#### 7.3.15. Map.Set
```
Puts an entry into this map with a given ttl (time to live) value.Entry will expire and get evicted after the ttl
If ttl is 0, then the entry lives forever. Similar to the put operation except that set doesn't
return the old value, which is more efficient.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x010f00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | New value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x010f01

Header only response message, no message body exist.

#### 7.3.16. Map.Lock
```
Acquires the lock for the specified lease time.After lease time, lock will be released.If the lock is not
available then the current thread becomes disabled for thread scheduling purposes and lies dormant until the lock
has been acquired.
Scope of the lock is this map only. Acquired lock is only for the key in this map. Locks are re-entrant,
so if the key is locked N times then it should be unlocked N times before another thread can acquire it.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011000

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |
| referenceId | long | False | The client-wide unique id for this request. It is used to make the request idempotent by sending the same reference id during retries. | 2.0 |

#### Response Message
**Message Type:** 0x011001

Header only response message, no message body exist.

#### 7.3.17. Map.TryLock
```
Tries to acquire the lock for the specified key for the specified lease time.After lease time, the lock will be
released.If the lock is not available, then the current thread becomes disabled for thread scheduling
purposes and lies dormant until one of two things happens the lock is acquired by the current thread, or
the specified waiting time elapses.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011100

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| lease | long | False | time in milliseconds to wait before releasing the lock. | 2.0 |
| timeout | long | False | maximum time to wait for getting the lock. | 2.0 |
| referenceId | long | False | The client-wide unique id for this request. It is used to make the request idempotent by sending the same reference id during retries. | 2.0 |

#### Response Message
**Message Type:** 0x011101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if successful, otherwise returns false | 2.0 |

#### 7.3.18. Map.IsLocked
```
Checks the lock for the specified key.If the lock is acquired then returns true, else returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011200

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| key | Data | False | Key for the map entry to check if it is locked. | 2.0 |

#### Response Message
**Message Type:** 0x011201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if the entry is locked, otherwise returns false | 2.0 |

#### 7.3.19. Map.Unlock
```
Releases the lock for the specified key. It never blocks and returns immediately.
If the current thread is the holder of this lock, then the hold count is decremented.If the hold count is zero,
then the lock is released.  If the current thread is not the holder of this lock,
then ILLEGAL_MONITOR_STATE is thrown.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011300

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| key | Data | False | Key for the map entry to unlock | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| referenceId | long | False | The client-wide unique id for this request. It is used to make the request idempotent by sending the same reference id during retries. | 2.0 |

#### Response Message
**Message Type:** 0x011301

Header only response message, no message body exist.

#### 7.3.20. Map.AddInterceptor
```
Adds an interceptor for this map. Added interceptor will intercept operations
and execute user defined methods and will cancel operations if user defined method throw exception.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| interceptor | Data | False | interceptor to add | 2.0 |

#### Response Message
**Message Type:** 0x011401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | String | False | id of registered interceptor. | 2.0 |

#### 7.3.21. Map.RemoveInterceptor
```
Removes the given interceptor for this map so it will not intercept operations anymore.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| id | String | False | of interceptor | 2.0 |

#### Response Message
**Message Type:** 0x011501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if successful, otherwise returns false | 2.0 |

#### 7.3.22. Map.AddEntryListenerToKeyWithPredicate
```
Adds a MapListener for this map. To receive an event, you should implement a corresponding MapListener
sub-interface for that event.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| predicate | Data | False | predicate for filtering entries. | 2.0 |
| includeValue | boolean | False | true if EntryEvent should contain the value. | 2.0 |
| listenerFlags | int | False | flags of enabled listeners. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x011601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x011603

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.3.23. Map.AddEntryListenerWithPredicate
```
Adds an continuous entry listener for this map. Listener will get notified for map add/remove/update/evict events
filtered by the given predicate.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| predicate | Data | False | predicate for filtering entries. | 2.0 |
| includeValue | boolean | False | true if EntryEvent should contain the value. | 2.0 |
| listenerFlags | int | False | flags of enabled listeners. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x011701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x011703

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.3.24. Map.AddEntryListenerToKey
```
Adds a MapListener for this map. To receive an event, you should implement a corresponding MapListener
sub-interface for that event.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| includeValue | boolean | False | true if EntryEvent should contain the value. | 2.0 |
| listenerFlags | int | False | flags of enabled listeners. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x011801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x011803

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.3.25. Map.AddEntryListener
```
Adds a MapListener for this map. To receive an event, you should implement a corresponding MapListener
sub-interface for that event.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| includeValue | boolean | False | true if EntryEvent should contain the value. | 2.0 |
| listenerFlags | int | False | flags of enabled listeners. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x011901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x011903

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.3.26. Map.RemoveEntryListener
```
Removes the specified entry listener. If there is no such listener added before, this call does no change in the
cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| registrationId | UUID | False | id of registered listener. | 2.0 |

#### Response Message
**Message Type:** 0x011a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if registration is removed, false otherwise. | 2.0 |

#### 7.3.27. Map.AddPartitionLostListener
```
Adds a MapPartitionLostListener. The addPartitionLostListener returns a register-id. This id is needed to remove
the MapPartitionLostListener using the removePartitionLostListener(String) method.
There is no check for duplicate registrations, so if you register the listener twice, it will get events twice.
IMPORTANT: Please see com.hazelcast.partition.PartitionLostListener for weaknesses.
IMPORTANT: Listeners registered from HazelcastClient may miss some of the map partition lost events due
to design limitations.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x011b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | returns the registration id for the MapPartitionLostListener. | 2.0 |

#### Event Message

##### MapPartitionLost
**Message Type:** 0x011b03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| partitionId | int | False | Id of the lost partition. | 2.0 |
| uuid | UUID | False | UUID of the member that owns the lost partition. | 2.0 |

#### 7.3.28. Map.RemovePartitionLostListener
```
Removes the specified map partition lost listener. If there is no such listener added before, this call does no
change in the cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| registrationId | UUID | False | id of register | 2.0 |

#### Response Message
**Message Type:** 0x011c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if registration is removed, false otherwise. | 2.0 |

#### 7.3.29. Map.GetEntryView
```
Returns the EntryView for the specified key.
This method returns a clone of original mapping, modifying the returned value does not change the actual value
in the map. One should put modified value back to make changes visible to all nodes.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011d00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| key | Data | False | the key of the entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x011d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | SimpleEntryView | True | Entry view of the specified key. | 2.0 |
| maxIdle | long | False | Last set max idle in millis. | 2.0 |

#### 7.3.30. Map.Evict
```
Evicts the specified key from this map. If a MapStore is defined for this map, then the entry is not deleted
from the underlying MapStore, evict only removes the entry from the memory.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011e00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| key | Data | False | the specified key to evict from this map. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x011e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the key is evicted, false otherwise. | 2.0 |

#### 7.3.31. Map.EvictAll
```
Evicts all keys from this map except the locked ones. If a MapStore is defined for this map, deleteAll is not
called by this method. If you do want to deleteAll to be called use the clear method. The EVICT_ALL event is
fired for any registered listeners.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x011f00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |

#### Response Message
**Message Type:** 0x011f01

Header only response message, no message body exist.

#### 7.3.32. Map.LoadAll
```
Loads all keys into the store. This is a batch load operation so that an implementation can optimize the multiple loads.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012000

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| replaceExistingValues | boolean | False | when <code>true</code>, existing values in the Map will be replaced by those loaded from the MapLoader | 2.0 |

#### Response Message
**Message Type:** 0x012001

Header only response message, no message body exist.

#### 7.3.33. Map.LoadGivenKeys
```
Loads the given keys. This is a batch load operation so that an implementation can optimize the multiple loads.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| keys | List of data | False | keys to load | 2.0 |
| replaceExistingValues | boolean | False | when <code>true</code>, existing values in the Map will be replaced by those loaded from the MapLoader | 2.0 |

#### Response Message
**Message Type:** 0x012101

Header only response message, no message body exist.

#### 7.3.34. Map.KeySet
```
Returns a set clone of the keys contained in this map. The set is NOT backed by the map, so changes to the map
are NOT reflected in the set, and vice-versa. This method is always executed by a distributed query, so it may
throw a QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the map | 2.0 |

#### Response Message
**Message Type:** 0x012201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | a set clone of the keys contained in this map. | 2.0 |

#### 7.3.35. Map.GetAll
```
Returns the entries for the given keys. If any keys are not present in the Map, it will call loadAll The returned
map is NOT backed by the original map, so changes to the original map are NOT reflected in the returned map, and vice-versa.
Please note that all the keys in the request should belong to the partition id to which this request is being sent, all keys
matching to a different partition id shall be ignored. The API implementation using this request may need to send multiple
of these request messages for filling a request for a key set if the keys belong to different partitions.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012300

**Partition Identifier:** Murmur hash of any key belongs to target partition % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| keys | List of data | False | keys to get | 2.0 |

#### Response Message
**Message Type:** 0x012301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | values for the provided keys. | 2.0 |

#### 7.3.36. Map.Values
```
Returns a collection clone of the values contained in this map.
The collection is NOT backed by the map, so changes to the map are NOT reflected in the collection, and vice-versa.
This method is always executed by a distributed query, so it may throw a QueryResultSizeExceededException
if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |

#### Response Message
**Message Type:** 0x012401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | All values in the map | 2.0 |

#### 7.3.37. Map.EntrySet
```
Returns a Set clone of the mappings contained in this map.
The collection is NOT backed by the map, so changes to the map are NOT reflected in the collection, and vice-versa.
This method is always executed by a distributed query, so it may throw a QueryResultSizeExceededException
if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |

#### Response Message
**Message Type:** 0x012501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | a set clone of the keys mappings in this map | 2.0 |

#### 7.3.38. Map.KeySetWithPredicate
```
Queries the map based on the specified predicate and returns the keys of matching entries. Specified predicate
runs on all members in parallel.The set is NOT backed by the map, so changes to the map are NOT reflected in the
set, and vice-versa. This method is always executed by a distributed query, so it may throw a
QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map. | 2.0 |
| predicate | Data | False | specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x012601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | result key set for the query. | 2.0 |

#### 7.3.39. Map.ValuesWithPredicate
```
Queries the map based on the specified predicate and returns the values of matching entries.Specified predicate
runs on all members in parallel. The collection is NOT backed by the map, so changes to the map are NOT reflected
in the collection, and vice-versa. This method is always executed by a distributed query, so it may throw a
QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| predicate | Data | False | specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x012701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | result value collection of the query. | 2.0 |

#### 7.3.40. Map.EntriesWithPredicate
```
Queries the map based on the specified predicate and returns the matching entries.Specified predicate
runs on all members in parallel. The collection is NOT backed by the map, so changes to the map are NOT reflected
in the collection, and vice-versa. This method is always executed by a distributed query, so it may throw a
QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| predicate | Data | False | specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x012801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | result key-value entry collection of the query. | 2.0 |

#### 7.3.41. Map.AddIndex
```
Adds an index to this map with specified configuration.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of map. | 2.0 |
| indexConfig | IndexConfig | False | Index configuration. | 2.0 |

#### Response Message
**Message Type:** 0x012901

Header only response message, no message body exist.

#### 7.3.42. Map.Size
```
Returns the number of key-value mappings in this map.  If the map contains more than Integer.MAX_VALUE elements,
returns Integer.MAX_VALUE

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | of map | 2.0 |

#### Response Message
**Message Type:** 0x012a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | the number of key-value mappings in this map | 2.0 |

#### 7.3.43. Map.IsEmpty
```
Returns true if this map contains no key-value mappings.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |

#### Response Message
**Message Type:** 0x012b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if this map contains no key-value mappings | 2.0 |

#### 7.3.44. Map.PutAll
```
Copies all of the mappings from the specified map to this map (optional operation).The effect of this call is
equivalent to that of calling put(Object,Object) put(k, v) on this map once for each mapping from key k to value
v in the specified map.The behavior of this operation is undefined if the specified map is modified while the
operation is in progress.
Please note that all the keys in the request should belong to the partition id to which this request is being sent, all keys
matching to a different partition id shall be ignored. The API implementation using this request may need to send multiple
of these request messages for filling a request for a key set if the keys belong to different partitions.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012c00

**Partition Identifier:** Murmur hash of any key belongs to target partition % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| entries | Map of data to data | False | mappings to be stored in this map | 2.0 |
| triggerMapLoader | boolean | False | should trigger MapLoader for elements not in this map | 2.1 |

#### Response Message
**Message Type:** 0x012c01

Header only response message, no message body exist.

#### 7.3.45. Map.Clear
```
This method clears the map and invokes MapStore#deleteAll deleteAll on MapStore which, if connected to a database,
will delete the records from that database. The MAP_CLEARED event is fired for any registered listeners.
To clear a map without calling MapStore#deleteAll, use #evictAll.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | of map | 2.0 |

#### Response Message
**Message Type:** 0x012d01

Header only response message, no message body exist.

#### 7.3.46. Map.ExecuteOnKey
```
Applies the user defined EntryProcessor to the entry mapped by the key. Returns the the object which is result of
the process() method of EntryProcessor.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012e00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| entryProcessor | Data | False | processor to execute on the map entry | 2.0 |
| key | Data | False | the key of the map entry. | 2.0 |
| threadId | long | False | Id of the thread that the task is submitted from. | 2.0 |

#### Response Message
**Message Type:** 0x012e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | result of entry process. | 2.0 |

#### 7.3.47. Map.SubmitToKey
```
Applies the user defined EntryProcessor to the entry mapped by the key. Returns immediately with a Future
representing that task.EntryProcessor is not cancellable, so calling Future.cancel() method won't cancel the
operation of EntryProcessor.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x012f00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| entryProcessor | Data | False | entry processor to be executed on the entry. | 2.0 |
| key | Data | False | the key of the map entry. | 2.0 |
| threadId | long | False | Id of the thread that the task is submitted from. | 2.0 |

#### Response Message
**Message Type:** 0x012f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | result of entry process. | 2.0 |

#### 7.3.48. Map.ExecuteOnAllKeys
```
Applies the user defined EntryProcessor to the all entries in the map.Returns the results mapped by each key in the map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013000

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| entryProcessor | Data | False | entry processor to be executed. | 2.0 |

#### Response Message
**Message Type:** 0x013001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | results of entry process on the entries | 2.0 |

#### 7.3.49. Map.ExecuteWithPredicate
```
Applies the user defined EntryProcessor to the entries in the map which satisfies provided predicate.
Returns the results mapped by each key in the map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| entryProcessor | Data | False | entry processor to be executed. | 2.0 |
| predicate | Data | False | specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x013101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | results of entry process on the entries matching the query criteria | 2.0 |

#### 7.3.50. Map.ExecuteOnKeys
```
Applies the user defined EntryProcessor to the entries mapped by the collection of keys.The results mapped by
each key in the collection.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| entryProcessor | Data | False | entry processor to be executed. | 2.0 |
| keys | List of data | False | The keys for the entries for which the entry processor shall be executed on. | 2.0 |

#### Response Message
**Message Type:** 0x013201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | results of entry process on the entries with the provided keys | 2.0 |

#### 7.3.51. Map.ForceUnlock
```
Releases the lock for the specified key regardless of the lock owner.It always successfully unlocks the key,
never blocks,and returns immediately.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013300

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| key | Data | False | the key of the map entry. | 2.0 |
| referenceId | long | False | The client-wide unique id for this request. It is used to make the request idempotent by sending the same reference id during retries. | 2.0 |

#### Response Message
**Message Type:** 0x013301

Header only response message, no message body exist.

#### 7.3.52. Map.KeySetWithPagingPredicate
```
Queries the map based on the specified predicate and returns the keys of matching entries. Specified predicate
runs on all members in parallel. The collection is NOT backed by the map, so changes to the map are NOT reflected
in the collection, and vice-versa. This method is always executed by a distributed query, so it may throw a
QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| predicate | PagingPredicateHolder | False | specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x013401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | result keys for the query. | 2.0 |
| anchorDataList | AnchorDataListHolder | False | The updated anchor list. | 2.0 |

#### 7.3.53. Map.ValuesWithPagingPredicate
```
Queries the map based on the specified predicate and returns the values of matching entries. Specified predicate
runs on all members in parallel. The collection is NOT backed by the map, so changes to the map are NOT reflected
in the collection, and vice-versa. This method is always executed by a distributed query, so it may throw a
QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| predicate | PagingPredicateHolder | False | specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x013501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | values for the query. | 2.0 |
| anchorDataList | AnchorDataListHolder | False | The updated anchor list. | 2.0 |

#### 7.3.54. Map.EntriesWithPagingPredicate
```
Queries the map based on the specified predicate and returns the matching entries. Specified predicate
runs on all members in parallel. The collection is NOT backed by the map, so changes to the map are NOT reflected
in the collection, and vice-versa. This method is always executed by a distributed query, so it may throw a
QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.0 |
| predicate | PagingPredicateHolder | False | specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x013601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | key-value pairs for the query. | 2.0 |
| anchorDataList | AnchorDataListHolder | False | The updated anchor list. | 2.0 |

#### 7.3.55. Map.FetchKeys
```
Fetches specified number of keys from the specified partition starting from specified table index.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013700

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| batch | int | False | The number of items to be batched | 2.0 |

#### Response Message
**Message Type:** 0x013701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| keys | List of data | False | List of keys. | 2.0 |

#### 7.3.56. Map.FetchEntries
```
Fetches specified number of entries from the specified partition starting from specified table index.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013800

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| batch | int | False | The number of items to be batched | 2.0 |

#### Response Message
**Message Type:** 0x013801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| entries | Map of data to data | False | List of entries. | 2.0 |

#### 7.3.57. Map.Aggregate
```
Applies the aggregation logic on all map entries and returns the result

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| aggregator | Data | False | aggregator to aggregate the entries with | 2.0 |

#### Response Message
**Message Type:** 0x013901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | the aggregation result | 2.0 |

#### 7.3.58. Map.AggregateWithPredicate
```
Applies the aggregation logic on map entries filtered with the Predicate and returns the result

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| aggregator | Data | False | aggregator to aggregate the entries with | 2.0 |
| predicate | Data | False | predicate to filter the entries with | 2.0 |

#### Response Message
**Message Type:** 0x013a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | the aggregation result | 2.0 |

#### 7.3.59. Map.Project
```
Applies the projection logic on all map entries and returns the result

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| projection | Data | False | projection to transform the entries with. May return null. | 2.0 |

#### Response Message
**Message Type:** 0x013b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | the resulted collection upon transformation to the type of the projection | 2.0 |

#### 7.3.60. Map.ProjectWithPredicate
```
Applies the projection logic on map entries filtered with the Predicate and returns the result

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| projection | Data | False | projection to transform the entries with. May return null. | 2.0 |
| predicate | Data | False | predicate to filter the entries with | 2.0 |

#### Response Message
**Message Type:** 0x013c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | the resulted collection upon transformation to the type of the projection | 2.0 |

#### 7.3.61. Map.FetchNearCacheInvalidationMetadata
```
Fetches invalidation metadata from partitions of map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| names | List of string | False | names of the maps | 2.0 |
| uuid | UUID | False | The uuid of the member to fetch the near cache invalidation meta data | 2.0 |

#### Response Message
**Message Type:** 0x013d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| namePartitionSequenceList | Map of string to entryList_Integer_Long | False | Map of partition ids and sequence number of invalidations mapped by the map name. | 2.0 |
| partitionUuidList | Map of integer to uUID | False | Map of member UUIDs mapped by the partition ids of invalidations. | 2.0 |

#### 7.3.62. Map.RemoveAll
```
Removes all entries which match with the supplied predicate

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | map name. | 2.0 |
| predicate | Data | False | used to select entries to be removed from map. | 2.0 |

#### Response Message
**Message Type:** 0x013e01

Header only response message, no message body exist.

#### 7.3.63. Map.AddNearCacheInvalidationListener
```
Adds listener to map. This listener will be used to listen near cache invalidation events.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x013f00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the map | 2.0 |
| listenerFlags | int | False | flags of enabled listeners. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x013f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### IMapInvalidation
**Message Type:** 0x013f03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | The key of the invalidated entry. | 2.0 |
| sourceUuid | UUID | False | UUID of the member who fired this event. | 2.0 |
| partitionUuid | UUID | False | UUID of the source partition that invalidated entry belongs to. | 2.0 |
| sequence | long | False | Sequence number of the invalidation event. | 2.0 |

##### IMapBatchInvalidation
**Message Type:** 0x013f04

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| keys | List of data | False | List of the keys of the invalidated entries. | 2.0 |
| sourceUuids | List of uUID | False | List of UUIDs of the members who fired these events. | 2.0 |
| partitionUuids | List of uUID | False | List of UUIDs of the source partitions that invalidated entries belong to. | 2.0 |
| sequences | List of long | False | List of sequence numbers of the invalidation events. | 2.0 |

#### 7.3.64. Map.FetchWithQuery
```
Fetches the specified number of entries from the specified partition starting from specified table index
that match the predicate and applies the projection logic on them.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x014000

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map | 2.0 |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| batch | int | False | The number of items to be batched | 2.0 |
| projection | Data | False | projection to transform the entries with | 2.0 |
| predicate | Data | False | predicate to filter the entries with | 2.0 |

#### Response Message
**Message Type:** 0x014001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| results | List of data | False | List of fetched entries. | 2.0 |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |

#### 7.3.65. Map.EventJournalSubscribe
```
Performs the initial subscription to the map event journal.
This includes retrieving the event journal sequences of the
oldest and newest event in the journal.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x014100

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the map | 2.0 |

#### Response Message
**Message Type:** 0x014101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| oldestSequence | long | False | Sequence id of the oldest event in the event journal. | 2.0 |
| newestSequence | long | False | Sequence id of the newest event in the event journal. | 2.0 |

#### 7.3.66. Map.EventJournalRead
```
Reads from the map event journal in batches. You may specify the start sequence,
the minimum required number of items in the response, the maximum number of items
in the response, a predicate that the events should pass and a projection to
apply to the events in the journal.
If the event journal currently contains less events than {@code minSize}, the
call will wait until it has sufficient items.
The predicate, filter and projection may be {@code null} in which case all elements are returned
and no projection is applied.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x014200

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the map | 2.0 |
| startSequence | long | False | the startSequence of the first item to read | 2.0 |
| minSize | int | False | the minimum number of items to read. | 2.0 |
| maxSize | int | False | the maximum number of items to read. | 2.0 |
| predicate | Data | True | the predicate to apply before processing events | 2.0 |
| projection | Data | True | the projection to apply to journal events | 2.0 |

#### Response Message
**Message Type:** 0x014201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| readCount | int | False | Number of items that have been read. | 2.0 |
| items | List of data | False | List of items that have been read. | 2.0 |
| itemSeqs | longArray | True | Sequence numbers of items in the event journal. | 2.0 |
| nextSeq | long | False | Sequence number of the item following the last read item. | 2.0 |

#### 7.3.67. Map.SetTtl
```
Updates TTL (time to live) value of the entry specified by {@code key} with a new TTL value.
New TTL value is valid from this operation is invoked, not from the original creation of the entry.
If the entry does not exist or already expired, then this call has no effect.
<p>
The entry will expire and get evicted after the TTL. If the TTL is 0,
then the entry lives forever. If the TTL is negative, then the TTL
from the map configuration will be used (default: forever).

If there is no entry with key {@code key}, this call has no effect.

<b>Warning:</b>
<p>
Time resolution for TTL is seconds. The given TTL value is rounded to the next closest second value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x014300

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map | 2.0 |
| key | Data | False | Key for the map entry | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x014301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | 'true' if the entry is affected, 'false' otherwise | 2.0 |

#### 7.3.68. Map.PutWithMaxIdle
```
Puts an entry into this map with a given ttl (time to live) value.Entry will expire and get evicted after the ttl
If ttl is 0, then the entry lives forever.This method returns a clone of the previous value, not the original
(identically equal) value previously put into the map.Time resolution for TTL is seconds. The given TTL value is
rounded to the next closest second value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x014400

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | Value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |
| maxIdle | long | False | The duration of maximum idle for this entry. Milliseconds of idle, after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x014401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | old value of the entry | 2.0 |

#### 7.3.69. Map.PutTransientWithMaxIdle
```
Same as put except that MapStore, if defined, will not be called to store/persist the entry.
If ttl and maxIdle are 0, then the entry lives forever.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x014500

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | Value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |
| maxIdle | long | False | The duration of maximum idle for this entry. Milliseconds of idle, after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x014501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | old value of the entry | 2.0 |

#### 7.3.70. Map.PutIfAbsentWithMaxIdle
```
Puts an entry into this map with a given ttl (time to live) value if the specified key is not already associated
with a value. Entry will expire and get evicted after the ttl or maxIdle, whichever comes first.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x014600

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | Value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |
| maxIdle | long | False | The duration of maximum idle for this entry. Milliseconds of idle, after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x014601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | old value of the entry | 2.0 |

#### 7.3.71. Map.SetWithMaxIdle
```
Puts an entry into this map with a given ttl (time to live) value and maxIdle.
Entry will expire and get evicted after the ttl or maxIdle, whichever comes first.
If ttl and maxIdle are 0, then the entry lives forever.

Similar to the put operation except that set doesn't return the old value, which is more efficient.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x014700

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the map. | 2.0 |
| key | Data | False | Key for the map entry. | 2.0 |
| value | Data | False | Value for the map entry. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |
| maxIdle | long | False | The duration of maximum idle for this entry. Milliseconds of idle, after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x014701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | old value of the entry | 2.0 |

#### 7.3.72. Map.ReplaceAll
```
Replaces each entry's value with the result of invoking the given
function on that entry until all entries have been processed in the targetted partition
or the function throws an exception.

```

**Available since:** 2.4

#### Request Message
**Message Type:** 0x014800

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.4 |
| function | Data | False | the function to apply to each entry. | 2.4 |

#### Response Message
**Message Type:** 0x014801

Header only response message, no message body exist.

#### 7.3.73. Map.PutAllWithMetadata
```
Copies all of the mappings from the specified entry list to this map, including metadata.
The implementation uses MergeOperation with PassThroughMergePolicy, so the effect of 
this call is equivalent to synchronizing given entries using WAN replication.
Please note that all the keys in the request should belong to the partition id to which this request is being sent, all keys
matching to a different partition id shall be ignored. The API implementation using this request may need to send multiple
of these request messages for filling a request for a key set if the keys belong to different partitions.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x014900

**Partition Identifier:** Murmur hash of any key belongs to target partition % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.7 |
| entries | List of simpleEntryView | False | entries with metadata | 2.7 |

#### Response Message
**Message Type:** 0x014901

Header only response message, no message body exist.

### 7.4. MultiMap
**Service id:** 2

#### 7.4.1. MultiMap.Put
```
Stores a key-value pair in the multimap.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020100

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key to be stored | 2.0 |
| value | Data | False | The value to be stored | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x020101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if size of the multimap is increased, false if the multimap already contains the key-value pair. | 2.0 |

#### 7.4.2. MultiMap.Get
```
Returns the collection of values associated with the key. The collection is NOT backed by the map, so changes to
the map are NOT reflected in the collection, and vice-versa.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020200

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key whose associated values are to be returned | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x020201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | The collection of the values associated with the key. | 2.0 |

#### 7.4.3. MultiMap.Remove
```
Removes the given key value pair from the multimap.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020300

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key of the entry to remove | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x020301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | True if the size of the multimap changed after the remove operation, false otherwise. | 2.0 |

#### 7.4.4. MultiMap.KeySet
```
Returns the set of keys in the multimap.The collection is NOT backed by the map, so changes to the map are NOT
reflected in the collection, and vice-versa.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |

#### Response Message
**Message Type:** 0x020401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | The set of keys in the multimap. The returned set might be modifiable but it has no effect on the multimap. | 2.0 |

#### 7.4.5. MultiMap.Values
```
Returns the collection of values in the multimap.The collection is NOT backed by the map, so changes to the map
are NOT reflected in the collection, and vice-versa.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |

#### Response Message
**Message Type:** 0x020501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | The collection of values in the multimap. the returned collection might be modifiable but it has no effect on the multimap. | 2.0 |

#### 7.4.6. MultiMap.EntrySet
```
Returns the set of key-value pairs in the multimap.The collection is NOT backed by the map, so changes to the map
are NOT reflected in the collection, and vice-versa

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |

#### Response Message
**Message Type:** 0x020601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | The set of key-value pairs in the multimap. The returned set might be modifiable but it has no effect on the multimap. | 2.0 |

#### 7.4.7. MultiMap.ContainsKey
```
Returns whether the multimap contains an entry with the key.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020700

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key whose existence is checked. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x020701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the multimap contains an entry with the key, false otherwise. | 2.0 |

#### 7.4.8. MultiMap.ContainsValue
```
Returns whether the multimap contains an entry with the value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| value | Data | False | The value whose existence is checked. | 2.0 |

#### Response Message
**Message Type:** 0x020801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the multimap contains an entry with the value, false otherwise. | 2.0 |

#### 7.4.9. MultiMap.ContainsEntry
```
Returns whether the multimap contains the given key-value pair.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020900

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key whose existence is checked. | 2.0 |
| value | Data | False | The value whose existence is checked. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation | 2.0 |

#### Response Message
**Message Type:** 0x020901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the multimap contains the key-value pair, false otherwise. | 2.0 |

#### 7.4.10. MultiMap.Size
```
Returns the number of key-value pairs in the multimap.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |

#### Response Message
**Message Type:** 0x020a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of key-value pairs in the multimap. | 2.0 |

#### 7.4.11. MultiMap.Clear
```
Clears the multimap. Removes all key-value pairs.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |

#### Response Message
**Message Type:** 0x020b01

Header only response message, no message body exist.

#### 7.4.12. MultiMap.ValueCount
```
Returns the number of values that match the given key in the multimap.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key whose values count is to be returned | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation | 2.0 |

#### Response Message
**Message Type:** 0x020c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of values that match the given key in the multimap | 2.0 |

#### 7.4.13. MultiMap.AddEntryListenerToKey
```
Adds the specified entry listener for the specified key.The listener will be notified for all
add/remove/update/evict events for the specified key only.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key to listen to | 2.0 |
| includeValue | boolean | False | True if EntryEvent should contain the value,false otherwise | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x020d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Returns registration id for the entry listener | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x020d03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.4.14. MultiMap.AddEntryListener
```
Adds an entry listener for this multimap. The listener will be notified for all multimap add/remove/update/evict events.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| includeValue | boolean | False | True if EntryEvent should contain the value,false otherwise | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x020e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Returns registration id for the entry listener | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x020e03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.4.15. MultiMap.RemoveEntryListener
```
Removes the specified entry listener. If there is no such listener added before, this call does no change in the
cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x020f00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| registrationId | UUID | False | Registration id of listener | 2.0 |

#### Response Message
**Message Type:** 0x020f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if registration is removed, false otherwise | 2.0 |

#### 7.4.16. MultiMap.Lock
```
Acquires the lock for the specified key for the specified lease time. After the lease time, the lock will be
released. If the lock is not available, then the current thread becomes disabled for thread scheduling
purposes and lies dormant until the lock has been acquired. Scope of the lock is for this map only. The acquired
lock is only for the key in this map.Locks are re-entrant, so if the key is locked N times, then it should be
unlocked N times before another thread can acquire it.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x021000

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key the Lock | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |
| referenceId | long | False | The client-wide unique id for this request. It is used to make the request idempotent by sending the same reference id during retries. | 2.0 |

#### Response Message
**Message Type:** 0x021001

Header only response message, no message body exist.

#### 7.4.17. MultiMap.TryLock
```
Tries to acquire the lock for the specified key for the specified lease time. After lease time, the lock will be
released. If the lock is not available, then the current thread becomes disabled for thread scheduling purposes
and lies dormant until one of two things happens:the lock is acquired by the current thread, or the specified
waiting time elapses.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x021100

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | Key to lock in this map. | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation | 2.0 |
| lease | long | False | Time in milliseconds to wait before releasing the lock. | 2.0 |
| timeout | long | False | Maximum time to wait for the lock. | 2.0 |
| referenceId | long | False | The client-wide unique id for this request. It is used to make the request idempotent by sending the same reference id during retries. | 2.0 |

#### Response Message
**Message Type:** 0x021101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the lock was acquired and false if the waiting time elapsed before the lock acquired | 2.0 |

#### 7.4.18. MultiMap.IsLocked
```
Checks the lock for the specified key. If the lock is acquired, this method returns true, else it returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x021200

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | Key to lock to be checked. | 2.0 |

#### Response Message
**Message Type:** 0x021201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the lock acquired,false otherwise | 2.0 |

#### 7.4.19. MultiMap.Unlock
```
Releases the lock for the specified key regardless of the lock owner. It always successfully unlocks the key,
never blocks and returns immediately.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x021300

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key to Lock | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation | 2.0 |
| referenceId | long | False | The client-wide unique id for this request. It is used to make the request idempotent by sending the same reference id during retries. | 2.0 |

#### Response Message
**Message Type:** 0x021301

Header only response message, no message body exist.

#### 7.4.20. MultiMap.ForceUnlock
```
Releases the lock for the specified key regardless of the lock owner. It always successfully unlocks the key,
never blocks and returns immediately.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x021400

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key to Lock | 2.0 |
| referenceId | long | False | The client-wide unique id for this request. It is used to make the request idempotent by sending the same reference id during retries. | 2.0 |

#### Response Message
**Message Type:** 0x021401

Header only response message, no message body exist.

#### 7.4.21. MultiMap.RemoveEntry
```
Removes all the entries with the given key. The collection is NOT backed by the map, so changes to the map are
NOT reflected in the collection, and vice-versa.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x021500

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key of the entry to remove | 2.0 |
| value | Data | False | The value of the entry to remove | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation | 2.0 |

#### Response Message
**Message Type:** 0x021501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the size of the multimap changed after the remove operation, false otherwise. | 2.0 |

#### 7.4.22. MultiMap.Delete
```
Removes all the entries with the given key.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x021600

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the MultiMap | 2.0 |
| key | Data | False | The key of the entry to remove | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation | 2.0 |

#### Response Message
**Message Type:** 0x021601

Header only response message, no message body exist.

#### 7.4.23. MultiMap.PutAll
```
Copies all of the mappings from the specified map to this MultiMap. The effect of this call is
equivalent to that of calling put(k, v) on this MultiMap iteratively for each value in the mapping from key k to value
v in the specified MultiMap. The behavior of this operation is undefined if the specified map is modified while the
operation is in progress.

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x021700

**Partition Identifier:** Murmur hash of any key belongs to target partition % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of map | 2.1 |
| entries | Map of data to list_Data | False | mappings to be stored in this map | 2.1 |

#### Response Message
**Message Type:** 0x021701

Header only response message, no message body exist.

### 7.5. Queue
**Service id:** 3

#### 7.5.1. Queue.Offer
```
Inserts the specified element into this queue, waiting up to the specified wait time if necessary for space to
become available.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030100

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| value | Data | False | The element to add | 2.0 |
| timeoutMillis | long | False | Maximum time in milliseconds to wait for acquiring the lock for the key. | 2.0 |

#### Response Message
**Message Type:** 0x030101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>True</tt> if the element was added to this queue, else <tt>false</tt> | 2.0 |

#### 7.5.2. Queue.Put
```
Inserts the specified element into this queue, waiting if necessary for space to become available.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030200

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| value | Data | False | The element to add | 2.0 |

#### Response Message
**Message Type:** 0x030201

Header only response message, no message body exist.

#### 7.5.3. Queue.Size
```
Returns the number of elements in this collection.  If this collection contains more than Integer.MAX_VALUE
elements, returns Integer.MAX_VALUE

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030300

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |

#### Response Message
**Message Type:** 0x030301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of elements in this collection | 2.0 |

#### 7.5.4. Queue.Remove
```
Retrieves and removes the head of this queue.  This method differs from poll only in that it throws an exception
if this queue is empty.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030400

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| value | Data | False | Element to be removed from this queue, if present | 2.0 |

#### Response Message
**Message Type:** 0x030401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if this queue changed as a result of the call | 2.0 |

#### 7.5.5. Queue.Poll
```
Retrieves and removes the head of this queue, waiting up to the specified wait time if necessary for an element
to become available.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030500

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| timeoutMillis | long | False | Maximum time in milliseconds to wait for acquiring the lock for the key. | 2.0 |

#### Response Message
**Message Type:** 0x030501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The head of this queue, or <tt>null</tt> if this queue is empty | 2.0 |

#### 7.5.6. Queue.Take
```
Retrieves and removes the head of this queue, waiting if necessary until an element becomes available.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030600

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |

#### Response Message
**Message Type:** 0x030601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The head of this queue | 2.0 |

#### 7.5.7. Queue.Peek
```
Retrieves, but does not remove, the head of this queue, or returns null if this queue is empty.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030700

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |

#### Response Message
**Message Type:** 0x030701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The head of this queue, or <tt>null</tt> if this queue is empty | 2.0 |

#### 7.5.8. Queue.Iterator
```
Returns an iterator over the elements in this collection.  There are no guarantees concerning the order in which
the elements are returned (unless this collection is an instance of some class that provides a guarantee).

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030800

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |

#### Response Message
**Message Type:** 0x030801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | list of all data in queue | 2.0 |

#### 7.5.9. Queue.DrainTo
```
Removes all available elements from this queue and adds them to the given collection.  This operation may be more
efficient than repeatedly polling this queue.  A failure encountered while attempting to add elements to
collection c may result in elements being in neither, either or both collections when the associated exception is
thrown. Attempts to drain a queue to itself result in ILLEGAL_ARGUMENT. Further, the behavior of
this operation is undefined if the specified collection is modified while the operation is in progress.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030900

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |

#### Response Message
**Message Type:** 0x030901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | list of all removed data in queue | 2.0 |

#### 7.5.10. Queue.DrainToMaxSize
```
Removes at most the given number of available elements from this queue and adds them to the given collection.
A failure encountered while attempting to add elements to collection may result in elements being in neither,
either or both collections when the associated exception is thrown. Attempts to drain a queue to itself result in
ILLEGAL_ARGUMENT. Further, the behavior of this operation is undefined if the specified collection is
modified while the operation is in progress.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030a00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| maxSize | int | False | The maximum number of elements to transfer | 2.0 |

#### Response Message
**Message Type:** 0x030a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | list of all removed data in result of this method | 2.0 |

#### 7.5.11. Queue.Contains
```
Returns true if this queue contains the specified element. More formally, returns true if and only if this queue
contains at least one element e such that value.equals(e)

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030b00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| value | Data | False | Element whose presence in this collection is to be tested | 2.0 |

#### Response Message
**Message Type:** 0x030b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if this collection contains the specified element | 2.0 |

#### 7.5.12. Queue.ContainsAll
```
Return true if this collection contains all of the elements in the specified collection.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030c00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| dataList | List of data | False | Collection to be checked for containment in this collection | 2.0 |

#### Response Message
**Message Type:** 0x030c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if this collection contains all of the elements in the specified collection | 2.0 |

#### 7.5.13. Queue.CompareAndRemoveAll
```
Removes all of this collection's elements that are also contained in the specified collection (optional operation).
After this call returns, this collection will contain no elements in common with the specified collection.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030d00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| dataList | List of data | False | Collection containing elements to be removed from this collection | 2.0 |

#### Response Message
**Message Type:** 0x030d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if this collection changed as a result of the call | 2.0 |

#### 7.5.14. Queue.CompareAndRetainAll
```
Retains only the elements in this collection that are contained in the specified collection (optional operation).
In other words, removes from this collection all of its elements that are not contained in the specified collection.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030e00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| dataList | List of data | False | collection containing elements to be retained in this collection | 2.0 |

#### Response Message
**Message Type:** 0x030e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if this collection changed as a result of the call | 2.0 |

#### 7.5.15. Queue.Clear
```
Removes all of the elements from this collection (optional operation). The collection will be empty after this
method returns.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x030f00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |

#### Response Message
**Message Type:** 0x030f01

Header only response message, no message body exist.

#### 7.5.16. Queue.AddAll
```
Adds all of the elements in the specified collection to this collection (optional operation).The behavior of this
operation is undefined if the specified collection is modified while the operation is in progress.
(This implies that the behavior of this call is undefined if the specified collection is this collection,
and this collection is nonempty.)

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x031000

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| dataList | List of data | False | Collection containing elements to be added to this collection | 2.0 |

#### Response Message
**Message Type:** 0x031001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if this collection changed as a result of the call | 2.0 |

#### 7.5.17. Queue.AddListener
```
Adds an listener for this collection. Listener will be notified or all collection add/remove events.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x031100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| includeValue | boolean | False | <tt>true</tt> if the updated item should be passed to the item listener, <tt>false</tt> otherwise. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x031101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | The registration id | 2.0 |

#### Event Message

##### Item
**Message Type:** 0x031103

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| item | Data | True | Item that the event is fired for. | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches this event. | 2.0 |
| eventType | int | False | Type of the event. It is either ADDED(1) or REMOVED(2). | 2.0 |

#### 7.5.18. Queue.RemoveListener
```
Removes the specified item listener. If there is no such listener added before, this call does no change in the
cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x031200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |
| registrationId | UUID | False | Id of the listener registration. | 2.0 |

#### Response Message
**Message Type:** 0x031201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the item listener is removed, false otherwise | 2.0 |

#### 7.5.19. Queue.RemainingCapacity
```
Returns the number of additional elements that this queue can ideally (in the absence of memory or resource
constraints) accept without blocking, or Integer.MAX_VALUE if there is no intrinsic limit. Note that you cannot
always tell if an attempt to insert an element will succeed by inspecting remainingCapacity because it may be
the case that another thread is about to insert or remove an element.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x031300

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |

#### Response Message
**Message Type:** 0x031301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The remaining capacity | 2.0 |

#### 7.5.20. Queue.IsEmpty
```
Returns true if this collection contains no elements.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x031400

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Queue | 2.0 |

#### Response Message
**Message Type:** 0x031401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>True</tt> if this collection contains no elements | 2.0 |

### 7.6. Topic
**Service id:** 4

#### 7.6.1. Topic.Publish
```
Publishes the message to all subscribers of this topic

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x040100

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Topic | 2.0 |
| message | Data | False | The message to publish to all subscribers of this topic | 2.0 |

#### Response Message
**Message Type:** 0x040101

Header only response message, no message body exist.

#### 7.6.2. Topic.AddMessageListener
```
Subscribes to this topic. When someone publishes a message on this topic. onMessage() function of the given
MessageListener is called. More than one message listener can be added on one instance.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x040200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Topic | 2.0 |
| localOnly | boolean | False | if true listens only local events on registered member | 2.0 |

#### Response Message
**Message Type:** 0x040201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | returns the registration id | 2.0 |

#### Event Message

##### Topic
**Message Type:** 0x040203

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| item | Data | False | Item that the event is fired for. | 2.0 |
| publishTime | long | False | Time that the item is published to the topic. | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches this event. | 2.0 |

#### 7.6.3. Topic.RemoveMessageListener
```
Stops receiving messages for the given message listener.If the given listener already removed, this method does nothing.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x040300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Topic | 2.0 |
| registrationId | UUID | False | Id of listener registration. | 2.0 |

#### Response Message
**Message Type:** 0x040301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if registration is removed, false otherwise | 2.0 |

#### 7.6.4. Topic.PublishAll
```
Publishes all messages to all subscribers of this topic

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x040400

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Topic | 2.1 |
| messages | List of data | False | The messages to publish to all subscribers of this topic | 2.1 |

#### Response Message
**Message Type:** 0x040401

Header only response message, no message body exist.

### 7.7. List
**Service id:** 5

#### 7.7.1. List.Size
```
Returns the number of elements in this list.  If this list contains more than Integer.MAX_VALUE elements, returns
Integer.MAX_VALUE.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050100

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of List | 2.0 |

#### Response Message
**Message Type:** 0x050101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of elements in this list | 2.0 |

#### 7.7.2. List.Contains
```
Returns true if this list contains the specified element.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050200

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| value | Data | False | Element whose presence in this list is to be tested | 2.0 |

#### Response Message
**Message Type:** 0x050201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this list contains the specified element, false otherwise | 2.0 |

#### 7.7.3. List.ContainsAll
```
Returns true if this list contains all of the elements of the specified collection.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050300

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| values | List of data | False | Collection to be checked for containment in this list | 2.0 |

#### Response Message
**Message Type:** 0x050301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this list contains all of the elements of the specified collection | 2.0 |

#### 7.7.4. List.Add
```
Appends the specified element to the end of this list (optional operation). Lists that support this operation may
place limitations on what elements may be added to this list.  In particular, some lists will refuse to add null
elements, and others will impose restrictions on the type of elements that may be added. List classes should
clearly specify in their documentation any restrictions on what elements may be added.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050400

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| value | Data | False | Element to be appended to this list | 2.0 |

#### Response Message
**Message Type:** 0x050401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if this list changed as a result of the call, false otherwise | 2.0 |

#### 7.7.5. List.Remove
```
Removes the first occurrence of the specified element from this list, if it is present (optional operation).
If this list does not contain the element, it is unchanged.
Returns true if this list contained the specified element (or equivalently, if this list changed as a result of the call).

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050500

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| value | Data | False | Element to be removed from this list, if present | 2.0 |

#### Response Message
**Message Type:** 0x050501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this list contained the specified element, false otherwise | 2.0 |

#### 7.7.6. List.AddAll
```
Appends all of the elements in the specified collection to the end of this list, in the order that they are
returned by the specified collection's iterator (optional operation).
The behavior of this operation is undefined if the specified collection is modified while the operation is in progress.
(Note that this will occur if the specified collection is this list, and it's nonempty.)

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050600

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| valueList | List of data | False | Collection containing elements to be added to this list | 2.0 |

#### Response Message
**Message Type:** 0x050601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this list changed as a result of the call, false otherwise | 2.0 |

#### 7.7.7. List.CompareAndRemoveAll
```
Removes from this list all of its elements that are contained in the specified collection (optional operation).

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050700

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| values | List of data | False | The list of values to compare for removal. | 2.0 |

#### Response Message
**Message Type:** 0x050701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if removed at least one of the items, false otherwise. | 2.0 |

#### 7.7.8. List.CompareAndRetainAll
```
Retains only the elements in this list that are contained in the specified collection (optional operation).
In other words, removes from this list all of its elements that are not contained in the specified collection.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050800

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| values | List of data | False | The list of values to compare for retaining. | 2.0 |

#### Response Message
**Message Type:** 0x050801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this list changed as a result of the call, false otherwise. | 2.0 |

#### 7.7.9. List.Clear
```
Removes all of the elements from this list (optional operation). The list will be empty after this call returns.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050900

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |

#### Response Message
**Message Type:** 0x050901

Header only response message, no message body exist.

#### 7.7.10. List.GetAll
```
Return the all elements of this collection

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050a00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |

#### Response Message
**Message Type:** 0x050a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | An array of all item values in the list. | 2.0 |

#### 7.7.11. List.AddListener
```
Adds an item listener for this collection. Listener will be notified for all collection add/remove events.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050b00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| includeValue | boolean | False | Set to true if you want the event to contain the value. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x050b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Registration id for the listener. | 2.0 |

#### Event Message

##### Item
**Message Type:** 0x050b03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| item | Data | True | Item that the event is fired for. | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches this event. | 2.0 |
| eventType | int | False | Type of the event. It is either ADDED(1) or REMOVED(2). | 2.0 |

#### 7.7.12. List.RemoveListener
```
Removes the specified item listener. If there is no such listener added before, this call does no change in the
cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050c00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| registrationId | UUID | False | The id of the listener which was provided during registration. | 2.0 |

#### Response Message
**Message Type:** 0x050c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if unregistered, false otherwise. | 2.0 |

#### 7.7.13. List.IsEmpty
```
Returns true if this list contains no elements

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050d00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |

#### Response Message
**Message Type:** 0x050d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this list contains no elements | 2.0 |

#### 7.7.14. List.AddAllWithIndex
```
Inserts all of the elements in the specified collection into this list at the specified position (optional operation).
Shifts the element currently at that position (if any) and any subsequent elements to the right (increases their indices).
The new elements will appear in this list in the order that they are returned by the specified collection's iterator.
The behavior of this operation is undefined if the specified collection is modified while the operation is in progress.
(Note that this will occur if the specified collection is this list, and it's nonempty.)

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050e00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| index | int | False | index at which to insert the first element from the specified collection. | 2.0 |
| valueList | List of data | False | The list of value to insert into the list. | 2.0 |

#### Response Message
**Message Type:** 0x050e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this list changed as a result of the call, false otherwise. | 2.0 |

#### 7.7.15. List.Get
```
Returns the element at the specified position in this list

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x050f00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| index | int | False | Index of the element to return | 2.0 |

#### Response Message
**Message Type:** 0x050f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The element at the specified position in this list | 2.0 |

#### 7.7.16. List.Set
```
The element previously at the specified position

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x051000

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| index | int | False | Index of the element to replace | 2.0 |
| value | Data | False | Element to be stored at the specified position | 2.0 |

#### Response Message
**Message Type:** 0x051001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The element previously at the specified position | 2.0 |

#### 7.7.17. List.AddWithIndex
```
Inserts the specified element at the specified position in this list (optional operation). Shifts the element
currently at that position (if any) and any subsequent elements to the right (adds one to their indices).

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x051100

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| index | int | False | index at which the specified element is to be inserted | 2.0 |
| value | Data | False | Value to be inserted. | 2.0 |

#### Response Message
**Message Type:** 0x051101

Header only response message, no message body exist.

#### 7.7.18. List.RemoveWithIndex
```
Removes the element at the specified position in this list (optional operation). Shifts any subsequent elements
to the left (subtracts one from their indices). Returns the element that was removed from the list.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x051200

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| index | int | False | The index of the element to be removed | 2.0 |

#### Response Message
**Message Type:** 0x051201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The element previously at the specified position | 2.0 |

#### 7.7.19. List.LastIndexOf
```
Returns the index of the last occurrence of the specified element in this list, or -1 if this list does not
contain the element.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x051300

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| value | Data | False | Element to search for | 2.0 |

#### Response Message
**Message Type:** 0x051301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | the index of the last occurrence of the specified element in this list, or -1 if this list does not contain the element | 2.0 |

#### 7.7.20. List.IndexOf
```
Returns the index of the first occurrence of the specified element in this list, or -1 if this list does not
contain the element.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x051400

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| value | Data | False | Element to search for | 2.0 |

#### Response Message
**Message Type:** 0x051401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The index of the first occurrence of the specified element in this list, or -1 if this list does not contain the element | 2.0 |

#### 7.7.21. List.Sub
```
Returns a view of the portion of this list between the specified from, inclusive, and to, exclusive.(If from and
to are equal, the returned list is empty.) The returned list is backed by this list, so non-structural changes in
the returned list are reflected in this list, and vice-versa. The returned list supports all of the optional list
operations supported by this list.
This method eliminates the need for explicit range operations (of the sort that commonly exist for arrays).
Any operation that expects a list can be used as a range operation by passing a subList view instead of a whole list.
Similar idioms may be constructed for indexOf and lastIndexOf, and all of the algorithms in the Collections class
can be applied to a subList.
The semantics of the list returned by this method become undefined if the backing list (i.e., this list) is
structurally modified in any way other than via the returned list.(Structural modifications are those that change
the size of this list, or otherwise perturb it in such a fashion that iterations in progress may yield incorrect results.)

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x051500

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| from | int | False | Low endpoint (inclusive) of the subList | 2.0 |
| to | int | False | High endpoint (exclusive) of the subList | 2.0 |

#### Response Message
**Message Type:** 0x051501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | A view of the specified range within this list | 2.0 |

#### 7.7.22. List.Iterator
```
Returns an iterator over the elements in this list in proper sequence.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x051600

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |

#### Response Message
**Message Type:** 0x051601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | An iterator over the elements in this list in proper sequence | 2.0 |

#### 7.7.23. List.ListIterator
```
Returns a list iterator over the elements in this list (in proper sequence), starting at the specified position
in the list. The specified index indicates the first element that would be returned by an initial call to
ListIterator#next next. An initial call to ListIterator#previous previous would return the element with the
specified index minus one.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x051700

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the List | 2.0 |
| index | int | False | index of the first element to be returned from the list iterator next | 2.0 |

#### Response Message
**Message Type:** 0x051701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | a list iterator over the elements in this list (in proper sequence), starting at the specified position in the list | 2.0 |

### 7.8. Set
**Service id:** 6

#### 7.8.1. Set.Size
```
Returns the number of elements in this set (its cardinality). If this set contains more than Integer.MAX_VALUE
elements, returns Integer.MAX_VALUE.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060100

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |

#### Response Message
**Message Type:** 0x060101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of elements in this set (its cardinality) | 2.0 |

#### 7.8.2. Set.Contains
```
Returns true if this set contains the specified element.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060200

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| value | Data | False | Element whose presence in this set is to be tested | 2.0 |

#### Response Message
**Message Type:** 0x060201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this set contains the specified element, false otherwise | 2.0 |

#### 7.8.3. Set.ContainsAll
```
Returns true if this set contains all of the elements of the specified collection. If the specified collection is
also a set, this method returns true if it is a subset of this set.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060300

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| items | List of data | False | Collection to be checked for containment in this list | 2.0 |

#### Response Message
**Message Type:** 0x060301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if this set contains all of the elements of the specified collection | 2.0 |

#### 7.8.4. Set.Add
```
Adds the specified element to this set if it is not already present (optional operation).
If this set already contains the element, the call leaves the set unchanged and returns false.In combination with
the restriction on constructors, this ensures that sets never contain duplicate elements.
The stipulation above does not imply that sets must accept all elements; sets may refuse to add any particular
element, including null, and throw an exception, as described in the specification for Collection
Individual set implementations should clearly document any restrictions on the elements that they may contain.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060400

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| value | Data | False | Element to be added to this set | 2.0 |

#### Response Message
**Message Type:** 0x060401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this set did not already contain the specified element and the element is added, returns false otherwise. | 2.0 |

#### 7.8.5. Set.Remove
```
Removes the specified element from this set if it is present (optional operation).
Returns true if this set contained the element (or equivalently, if this set changed as a result of the call).
(This set will not contain the element once the call returns.)

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060500

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| value | Data | False | Object to be removed from this set, if present | 2.0 |

#### Response Message
**Message Type:** 0x060501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this set contained the specified element and it is removed successfully | 2.0 |

#### 7.8.6. Set.AddAll
```
Adds all of the elements in the specified collection to this set if they're not already present
(optional operation). If the specified collection is also a set, the addAll operation effectively modifies this
set so that its value is the union of the two sets. The behavior of this operation is undefined if the specified
collection is modified while the operation is in progress.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060600

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| valueList | List of data | False | Collection containing elements to be added to this set | 2.0 |

#### Response Message
**Message Type:** 0x060601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this set changed as a result of the call | 2.0 |

#### 7.8.7. Set.CompareAndRemoveAll
```
Removes from this set all of its elements that are contained in the specified collection (optional operation).
If the specified collection is also a set, this operation effectively modifies this set so that its value is the
asymmetric set difference of the two sets.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060700

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| values | List of data | False | The list of values to test for matching the item to remove. | 2.0 |

#### Response Message
**Message Type:** 0x060701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if at least one item in values existed and removed, false otherwise. | 2.0 |

#### 7.8.8. Set.CompareAndRetainAll
```
Retains only the elements in this set that are contained in the specified collection (optional operation).
In other words, removes from this set all of its elements that are not contained in the specified collection.
If the specified collection is also a set, this operation effectively modifies this set so that its value is the
intersection of the two sets.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060800

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| values | List of data | False | The list of values to test for matching the item to retain. | 2.0 |

#### Response Message
**Message Type:** 0x060801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if at least one item in values existed and it is retained, false otherwise. All items not in valueSet but in the Set are removed. | 2.0 |

#### 7.8.9. Set.Clear
```
Removes all of the elements from this set (optional operation). The set will be empty after this call returns.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060900

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |

#### Response Message
**Message Type:** 0x060901

Header only response message, no message body exist.

#### 7.8.10. Set.GetAll
```
Return the all elements of this collection

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060a00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |

#### Response Message
**Message Type:** 0x060a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | Array of all values in the Set | 2.0 |

#### 7.8.11. Set.AddListener
```
Adds an item listener for this collection. Listener will be notified for all collection add/remove events.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| includeValue | boolean | False | if set to true, the event shall also include the value. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x060b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | The registration id. | 2.0 |

#### Event Message

##### Item
**Message Type:** 0x060b03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| item | Data | True | Item that the event is fired for. | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches this event. | 2.0 |
| eventType | int | False | Type of the event. It is either ADDED(1) or REMOVED(2). | 2.0 |

#### 7.8.12. Set.RemoveListener
```
Removes the specified item listener. If there is no such listener added before, this call does no change in the
cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |
| registrationId | UUID | False | The id retrieved during registration. | 2.0 |

#### Response Message
**Message Type:** 0x060c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the listener with the provided id existed and removed, false otherwise. | 2.0 |

#### 7.8.13. Set.IsEmpty
```
Returns true if this set contains no elements.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x060d00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Set | 2.0 |

#### Response Message
**Message Type:** 0x060d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this set contains no elements | 2.0 |

### 7.9. FencedLock
**Service id:** 7

#### 7.9.1. FencedLock.Lock
```
Acquires the given FencedLock on the given CP group. If the lock is
acquired, a valid fencing token (positive number) is returned. If not
acquired because of max reentrant entry limit, the call returns -1.
If the lock is held by some other endpoint when this method is called,
the caller thread is blocked until the lock is released. If the session
is closed between reentrant acquires, the call fails with
{@code LockOwnershipLostException}.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x070100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this FencedLock instance | 2.0 |
| name | String | False | Name of this FencedLock instance | 2.0 |
| sessionId | long | False | Session ID of the caller | 2.0 |
| threadId | long | False | ID of the caller thread | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |

#### Response Message
**Message Type:** 0x070101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | a valid fencing token (positive number) if the lock is acquired, otherwise -1. | 2.0 |

#### 7.9.2. FencedLock.TryLock
```
Attempts to acquire the given FencedLock on the given CP group.
If the lock is acquired, a valid fencing token (positive number) is
returned. If not acquired either because of max reentrant entry limit or
the lock is not free during the timeout duration, the call returns -1.
If the lock is held by some other endpoint when this method is called,
the caller thread is blocked until the lock is released or the timeout
duration passes. If the session is closed between reentrant acquires,
the call fails with {@code LockOwnershipLostException}.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x070200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this FencedLock instance | 2.0 |
| name | String | False | Name of this FencedLock instance | 2.0 |
| sessionId | long | False | Session ID of the caller | 2.0 |
| threadId | long | False | ID of the caller thread | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |
| timeoutMs | long | False | Duration to wait for lock acquire | 2.0 |

#### Response Message
**Message Type:** 0x070201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | a valid fencing token (positive number) if the lock is acquired, otherwise -1. | 2.0 |

#### 7.9.3. FencedLock.Unlock
```
Unlocks the given FencedLock on the given CP group. If the lock is
not acquired, the call fails with {@link IllegalMonitorStateException}.
If the session is closed while holding the lock, the call fails with
{@code LockOwnershipLostException}. Returns true if the lock is still
held by the caller after a successful unlock() call, false otherwise.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x070300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this FencedLock instance | 2.0 |
| name | String | False | Name of this FencedLock instance | 2.0 |
| sessionId | long | False | Session ID of the caller | 2.0 |
| threadId | long | False | ID of the caller thread | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |

#### Response Message
**Message Type:** 0x070301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the lock is still held by the caller after a successful unlock() call, false otherwise. | 2.0 |

#### 7.9.4. FencedLock.GetLockOwnership
```
Returns current lock ownership status of the given FencedLock instance.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x070400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this FencedLock instance | 2.0 |
| name | String | False | Name of this FencedLock instance | 2.0 |

#### Response Message
**Message Type:** 0x070401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| fence | long | False | Fence token of the lock | 2.0 |
| lockCount | int | False | Reentrant lock count | 2.0 |
| sessionId | long | False | Id of the session that holds the lock | 2.0 |
| threadId | long | False | Id of the thread that holds the lock | 2.0 |

### 7.10. ExecutorService
**Service id:** 8

#### 7.10.1. ExecutorService.Shutdown
```
Initiates an orderly shutdown in which previously submitted tasks are executed, but no new tasks will be accepted.
Invocation has no additional effect if already shut down.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x080100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |

#### Response Message
**Message Type:** 0x080101

Header only response message, no message body exist.

#### 7.10.2. ExecutorService.IsShutdown
```
Returns true if this executor has been shut down.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x080200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |

#### Response Message
**Message Type:** 0x080201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if this executor has been shut down | 2.0 |

#### 7.10.3. ExecutorService.CancelOnPartition
```
Cancels the task running on the member that owns the partition with the given id.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x080300

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| uuid | UUID | False | Unique id for the execution. | 2.0 |
| interrupt | boolean | False | If true, then the thread interrupt call can be used to cancel the thread, otherwise interrupt can not be used. | 2.0 |

#### Response Message
**Message Type:** 0x080301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if cancelled successfully, false otherwise. | 2.0 |

#### 7.10.4. ExecutorService.CancelOnMember
```
Cancels the task running on the member with the given address.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x080400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| uuid | UUID | False | Unique id for the execution. | 2.0 |
| memberUUID | UUID | False | The UUID of the member to execute the request on. | 2.0 |
| interrupt | boolean | False | If true, then the thread interrupt call can be used to cancel the thread, otherwise interrupt can not be used. | 2.0 |

#### Response Message
**Message Type:** 0x080401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if cancelled successfully, false otherwise. | 2.0 |

#### 7.10.5. ExecutorService.SubmitToPartition
```
Submits the task to the member that owns the partition with the given id.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x080500

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |
| uuid | UUID | False | Unique id for the execution. | 2.0 |
| callable | Data | False | The callable object to be executed. | 2.0 |

#### Response Message
**Message Type:** 0x080501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the callable execution. | 2.0 |

#### 7.10.6. ExecutorService.SubmitToMember
```
Submits the task to member specified by the address.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x080600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |
| uuid | UUID | False | Unique id for the execution. | 2.0 |
| callable | Data | False | The callable object to be executed. | 2.0 |
| memberUUID | UUID | False | The UUID of the member host on which the callable shall be executed on. | 2.0 |

#### Response Message
**Message Type:** 0x080601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the callable execution. | 2.0 |

### 7.11. AtomicLong
**Service id:** 9

#### 7.11.1. AtomicLong.Apply
```
Applies a function on the value, the actual stored value will not change

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x090100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicLong instance. | 2.0 |
| name | String | False | Name of this IAtomicLong instance. | 2.0 |
| function | Data | False | The function applied to the value and the value is not changed. | 2.0 |

#### Response Message
**Message Type:** 0x090101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the function application. | 2.0 |

#### 7.11.2. AtomicLong.Alter
```
Alters the currently stored value by applying a function on it.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x090200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicLong instance. | 2.0 |
| name | String | False | Name of this IAtomicLong instance. | 2.0 |
| function | Data | False | The function applied to the currently stored value. | 2.0 |
| returnValueType | int | False | 0 returns the old value, 1 returns the new value | 2.0 |

#### Response Message
**Message Type:** 0x090201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | The old or the new value depending on the returnValueType parameter. | 2.0 |

#### 7.11.3. AtomicLong.AddAndGet
```
Atomically adds the given value to the current value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x090300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicLong instance. | 2.0 |
| name | String | False | Name of this IAtomicLong instance. | 2.0 |
| delta | long | False | The value to add to the current value | 2.0 |

#### Response Message
**Message Type:** 0x090301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the updated value, the given value added to the current value | 2.0 |

#### 7.11.4. AtomicLong.CompareAndSet
```
Atomically sets the value to the given updated value only if the current
value the expected value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x090400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicLong instance. | 2.0 |
| name | String | False | Name of this IAtomicLong instance. | 2.0 |
| expected | long | False | The expected value | 2.0 |
| updated | long | False | The new value | 2.0 |

#### Response Message
**Message Type:** 0x090401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if successful; or false if the actual value was not equal to the expected value. | 2.0 |

#### 7.11.5. AtomicLong.Get
```
Gets the current value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x090500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicLong instance. | 2.0 |
| name | String | False | Name of this IAtomicLong instance. | 2.0 |

#### Response Message
**Message Type:** 0x090501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | The current value | 2.0 |

#### 7.11.6. AtomicLong.GetAndAdd
```
Atomically adds the given value to the current value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x090600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicLong instance. | 2.0 |
| name | String | False | Name of this IAtomicLong instance. | 2.0 |
| delta | long | False | The value to add to the current value | 2.0 |

#### Response Message
**Message Type:** 0x090601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the old value before the add | 2.0 |

#### 7.11.7. AtomicLong.GetAndSet
```
Atomically sets the given value and returns the old value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x090700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicLong instance. | 2.0 |
| name | String | False | Name of this IAtomicLong instance. | 2.0 |
| newValue | long | False | The new value | 2.0 |

#### Response Message
**Message Type:** 0x090701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the old value | 2.0 |

### 7.12. AtomicRef
**Service id:** 10

#### 7.12.1. AtomicRef.Apply
```
Applies a function on the value

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0a0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicReference instance. | 2.0 |
| name | String | False | The name of this IAtomicReference instance. | 2.0 |
| function | Data | False | The function applied to the value. | 2.0 |
| returnValueType | int | False | 0 returns no value, 1 returns the old value, 2 returns the new value | 2.0 |
| alter | boolean | False | Denotes whether result of the function will be set to the IAtomicRefInstance | 2.0 |

#### Response Message
**Message Type:** 0x0a0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the function application. | 2.0 |

#### 7.12.2. AtomicRef.CompareAndSet
```
Alters the currently stored value by applying a function on it.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0a0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicReference instance. | 2.0 |
| name | String | False | Name of this IAtomicReference instance. | 2.0 |
| oldValue | Data | True | The expected value | 2.0 |
| newValue | Data | True | The new value | 2.0 |

#### Response Message
**Message Type:** 0x0a0201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if successful; or false if the actual value was not equal to the expected value. | 2.0 |

#### 7.12.3. AtomicRef.Contains
```
Checks if the reference contains the value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0a0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicReference instance. | 2.0 |
| name | String | False | Name of this IAtomicReference instance. | 2.0 |
| value | Data | True | The value to check (is allowed to be null). | 2.0 |

#### Response Message
**Message Type:** 0x0a0301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the value is found, false otherwise. | 2.0 |

#### 7.12.4. AtomicRef.Get
```
Gets the current value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0a0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicReference instance. | 2.0 |
| name | String | False | Name of this IAtomicReference instance. | 2.0 |

#### Response Message
**Message Type:** 0x0a0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The current value | 2.0 |

#### 7.12.5. AtomicRef.Set
```
Atomically sets the given value

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0a0500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this IAtomicReference instance. | 2.0 |
| name | String | False | Name of this IAtomicReference instance. | 2.0 |
| newValue | Data | True | The value to set | 2.0 |
| returnOldValue | boolean | False | Denotes whether the old value is returned or not | 2.0 |

#### Response Message
**Message Type:** 0x0a0501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | the old value or null, depending on the { | 2.0 |

### 7.13. CountDownLatch
**Service id:** 11

#### 7.13.1. CountDownLatch.TrySetCount
```
Sets the count to the given value if the current count is zero.
If the count is not zero, then this method does nothing
and returns false

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0b0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this CountDownLatch instance | 2.0 |
| name | String | False | Name of the CountDownLatch instance | 2.0 |
| count | int | False | The number of times countDown must be invoked before threads can pass through await | 2.0 |

#### Response Message
**Message Type:** 0x0b0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the new count was set, false if the current count is not zero. | 2.0 |

#### 7.13.2. CountDownLatch.Await
```
Causes the current thread to wait until the latch has counted down
to zero, or an exception is thrown, or the specified waiting time
elapses. If the current count is zero then this method returns
immediately with the value true. If the current count is greater than
zero, then the current thread becomes disabled for thread scheduling
purposes and lies dormant until one of five things happen: the count
reaches zero due to invocations of the {@code countDown} method, this
ICountDownLatch instance is destroyed, the countdown owner becomes
disconnected, some other thread Thread#interrupt interrupts the current
thread, or the specified waiting time elapses. If the count reaches zero
then the method returns with the value true. If the current thread has
its interrupted status set on entry to this method, or is interrupted
while waiting, then {@code InterruptedException} is thrown
and the current thread's interrupted status is cleared. If the specified
waiting time elapses then the value false is returned.  If the time is
less than or equal to zero, the method will not wait at all.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0b0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this CountDownLatch instance | 2.0 |
| name | String | False | Name of this CountDownLatch instance | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |
| timeoutMs | long | False | The maximum time in milliseconds to wait | 2.0 |

#### Response Message
**Message Type:** 0x0b0201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the count reached zero, false if the waiting time elapsed before the count reached 0 | 2.0 |

#### 7.13.3. CountDownLatch.CountDown
```
Decrements the count of the latch, releasing all waiting threads if
the count reaches zero. If the current count is greater than zero, then
it is decremented. If the new count is zero: All waiting threads are
re-enabled for thread scheduling purposes, and Countdown owner is set to
null. If the current count equals zero, then nothing happens.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0b0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this CountDownLatch instance | 2.0 |
| name | String | False | Name of the CountDownLatch instance | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |
| expectedRound | int | False | The round this invocation will be performed on | 2.0 |

#### Response Message
**Message Type:** 0x0b0301

Header only response message, no message body exist.

#### 7.13.4. CountDownLatch.GetCount
```
Returns the current count.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0b0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this CountDownLatch instance | 2.0 |
| name | String | False | Name of the CountDownLatch instance | 2.0 |

#### Response Message
**Message Type:** 0x0b0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The current count of this CountDownLatch instance | 2.0 |

#### 7.13.5. CountDownLatch.GetRound
```
Returns the current round. A round completes when the count value
reaches to 0 and a new round starts afterwards.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0b0500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this CountDownLatch instance | 2.0 |
| name | String | False | Name of the CountDownLatch instance | 2.0 |

#### Response Message
**Message Type:** 0x0b0501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The current round of this CountDownLatch instance | 2.0 |

### 7.14. Semaphore
**Service id:** 12

#### 7.14.1. Semaphore.Init
```
Initializes the ISemaphore instance with the given permit number, if not
initialized before.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0c0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this ISemaphore instance | 2.0 |
| name | String | False | Name of this ISemaphore instance | 2.0 |
| permits | int | False | Number of permits to initialize this ISemaphore | 2.0 |

#### Response Message
**Message Type:** 0x0c0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the ISemaphore is initialized with this call | 2.0 |

#### 7.14.2. Semaphore.Acquire
```
Acquires the requested amount of permits if available, reducing
the number of available permits. If no enough permits are available,
then the current thread becomes disabled for thread scheduling purposes
and lies dormant until other threads release enough permits.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0c0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this ISemaphore instance | 2.0 |
| name | String | False | Name of this ISemaphore instance | 2.0 |
| sessionId | long | False | Session ID of the caller | 2.0 |
| threadId | long | False | ID of the caller thread | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |
| permits | int | False | number of permits to acquire | 2.0 |
| timeoutMs | long | False | Duration to wait for permit acquire | 2.0 |

#### Response Message
**Message Type:** 0x0c0201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if requested permits are acquired, false otherwise | 2.0 |

#### 7.14.3. Semaphore.Release
```
Releases the given number of permits and increases the number of
available permits by that amount.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0c0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this ISemaphore instance | 2.0 |
| name | String | False | Name of this ISemaphore instance | 2.0 |
| sessionId | long | False | Session ID of the caller | 2.0 |
| threadId | long | False | ID of the caller thread | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |
| permits | int | False | number of permits to release | 2.0 |

#### Response Message
**Message Type:** 0x0c0301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true | 2.0 |

#### 7.14.4. Semaphore.Drain
```
Acquires all available permits at once and returns immediately.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0c0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this ISemaphore instance | 2.0 |
| name | String | False | Name of this ISemaphore instance | 2.0 |
| sessionId | long | False | Session ID of the caller | 2.0 |
| threadId | long | False | ID of the caller thread | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |

#### Response Message
**Message Type:** 0x0c0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | number of acquired permits | 2.0 |

#### 7.14.5. Semaphore.Change
```
Increases or decreases the number of permits by the given value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0c0500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this ISemaphore instance | 2.0 |
| name | String | False | Name of this ISemaphore instance | 2.0 |
| sessionId | long | False | Session ID of the caller | 2.0 |
| threadId | long | False | ID of the caller thread | 2.0 |
| invocationUid | UUID | False | UID of this invocation | 2.0 |
| permits | int | False | number of permits to increase / decrease | 2.0 |

#### Response Message
**Message Type:** 0x0c0501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true | 2.0 |

#### 7.14.6. Semaphore.AvailablePermits
```
Returns the number of available permits.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0c0600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this ISemaphore instance | 2.0 |
| name | String | False | Name of this ISemaphore instance | 2.0 |

#### Response Message
**Message Type:** 0x0c0601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | number of available permits | 2.0 |

#### 7.14.7. Semaphore.GetSemaphoreType
```
Returns true if the semaphore is JDK compatible

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0c0700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| proxyName | String | False | Name of the ISemaphore proxy | 2.0 |

#### Response Message
**Message Type:** 0x0c0701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the semaphore is JDK compatible | 2.0 |

### 7.15. ReplicatedMap
**Service id:** 13

#### 7.15.1. ReplicatedMap.Put
```
Associates a given value to the specified key and replicates it to the cluster. If there is an old value, it will
be replaced by the specified one and returned from the call. In addition, you have to specify a ttl and its TimeUnit
to define when the value is outdated and thus should be removed from the replicated map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0100

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| key | Data | False | Key with which the specified value is to be associated. | 2.0 |
| value | Data | False | Value to be associated with the specified key | 2.0 |
| ttl | long | False | ttl in milliseconds to be associated with the specified key-value pair | 2.0 |

#### Response Message
**Message Type:** 0x0d0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The old value if existed for the key. | 2.0 |

#### 7.15.2. ReplicatedMap.Size
```
Returns the number of key-value mappings in this map. If the map contains more than Integer.MAX_VALUE elements,
returns Integer.MAX_VALUE.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0200

**Partition Identifier:** a random partition ID from `0` to `PARTITION_COUNT`(exclusive)


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |

#### Response Message
**Message Type:** 0x0d0201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | the number of key-value mappings in this map. | 2.0 |

#### 7.15.3. ReplicatedMap.IsEmpty
```
Return true if this map contains no key-value mappings

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0300

**Partition Identifier:** a random partition ID from `0` to `PARTITION_COUNT`(exclusive)


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |

#### Response Message
**Message Type:** 0x0d0301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>True</tt> if this map contains no key-value mappings | 2.0 |

#### 7.15.4. ReplicatedMap.ContainsKey
```
Returns true if this map contains a mapping for the specified key.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0400

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| key | Data | False | The key whose associated value is to be returned. | 2.0 |

#### Response Message
**Message Type:** 0x0d0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>True</tt> if this map contains a mapping for the specified key | 2.0 |

#### 7.15.5. ReplicatedMap.ContainsValue
```
Returns true if this map maps one or more keys to the specified value.
This operation will probably require time linear in the map size for most implementations of the Map interface.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0500

**Partition Identifier:** a random partition ID from `0` to `PARTITION_COUNT`(exclusive)


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| value | Data | False | value whose presence in this map is to be tested | 2.0 |

#### Response Message
**Message Type:** 0x0d0501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if this map maps one or more keys to the specified value | 2.0 |

#### 7.15.6. ReplicatedMap.Get
```
Returns the value to which the specified key is mapped, or null if this map contains no mapping for the key.
If this map permits null values, then a return value of null does not
necessarily indicate that the map contains no mapping for the key; it's also possible that the map
explicitly maps the key to null.  The #containsKey operation may be used to distinguish these two cases.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0600

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| key | Data | False | The key whose associated value is to be returned | 2.0 |

#### Response Message
**Message Type:** 0x0d0601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The value to which the specified key is mapped, or null if this map contains no mapping for the key | 2.0 |

#### 7.15.7. ReplicatedMap.Remove
```
Removes the mapping for a key from this map if it is present (optional operation). Returns the value to which this map previously associated the key,
or null if the map contained no mapping for the key. If this map permits null values, then a return value of
null does not necessarily indicate that the map contained no mapping for the key; it's also possible that the map
explicitly mapped the key to null. The map will not contain a mapping for the specified key once the call returns.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0700

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| key | Data | False | Key with which the specified value is to be associated. | 2.0 |

#### Response Message
**Message Type:** 0x0d0701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | the previous value associated with <tt>key</tt>, or <tt>null</tt> if there was no mapping for <tt>key</tt>. | 2.0 |

#### 7.15.8. ReplicatedMap.PutAll
```
Copies all of the mappings from the specified map to this map (optional operation). The effect of this call is
equivalent to that of calling put(Object,Object) put(k, v) on this map once for each mapping from key k to value
v in the specified map. The behavior of this operation is undefined if the specified map is modified while the
operation is in progress.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| entries | Map of data to data | False | entries to be stored in this map | 2.0 |

#### Response Message
**Message Type:** 0x0d0801

Header only response message, no message body exist.

#### 7.15.9. ReplicatedMap.Clear
```
The clear operation wipes data out of the replicated maps.It is the only synchronous remote operation in this
implementation, so be aware that this might be a slow operation. If some node fails on executing the operation,
it is retried for at most 3 times (on the failing nodes only). If it does not work after the third time, this
method throws a OPERATION_TIMEOUT back to the caller.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Replicated Map | 2.0 |

#### Response Message
**Message Type:** 0x0d0901

Header only response message, no message body exist.

#### 7.15.10. ReplicatedMap.AddEntryListenerToKeyWithPredicate
```
Adds an continuous entry listener for this map. The listener will be notified for map add/remove/update/evict
events filtered by the given predicate.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Replicated Map | 2.0 |
| key | Data | False | Key with which the specified value is to be associated. | 2.0 |
| predicate | Data | False | The predicate for filtering entries | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x0d0a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string  which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x0d0a03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.15.11. ReplicatedMap.AddEntryListenerWithPredicate
```
Adds an continuous entry listener for this map. The listener will be notified for map add/remove/update/evict
events filtered by the given predicate.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Replicated Map | 2.0 |
| predicate | Data | False | The predicate for filtering entries | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x0d0b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string  which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x0d0b03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.15.12. ReplicatedMap.AddEntryListenerToKey
```
Adds the specified entry listener for the specified key. The listener will be notified for all
add/remove/update/evict events of the specified key only.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Replicated Map | 2.0 |
| key | Data | False | Key with which the specified value is to be associated. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x0d0c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string  which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x0d0c03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.15.13. ReplicatedMap.AddEntryListener
```
Adds an entry listener for this map. The listener will be notified for all map add/remove/update/evict events.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x0d0d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string  which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x0d0d03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.15.14. ReplicatedMap.RemoveEntryListener
```
Removes the specified entry listener. If there is no such listener added before, this call does no change in the
cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| registrationId | UUID | False | ID of the registered entry listener. | 2.0 |

#### Response Message
**Message Type:** 0x0d0e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if registration is removed, false otherwise. | 2.0 |

#### 7.15.15. ReplicatedMap.KeySet
```
Returns a lazy Set view of the key contained in this map. A LazySet is optimized for querying speed
(preventing eager deserialization and hashing on HashSet insertion) and does NOT provide all operations.
Any kind of mutating function will throw an UNSUPPORTED_OPERATION. Same is true for operations
like java.util.Set#contains(Object) and java.util.Set#containsAll(java.util.Collection) which would result in
very poor performance if called repeatedly (for example, in a loop). If the use case is different from querying
the data, please copy the resulting set into a new java.util.HashSet.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d0f00

**Partition Identifier:** a random partition ID from `0` to `PARTITION_COUNT`(exclusive)


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |

#### Response Message
**Message Type:** 0x0d0f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | A lazy set view of the keys contained in this map. | 2.0 |

#### 7.15.16. ReplicatedMap.Values
```
Returns a lazy collection view of the values contained in this map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d1000

**Partition Identifier:** a random partition ID from `0` to `PARTITION_COUNT`(exclusive)


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |

#### Response Message
**Message Type:** 0x0d1001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | A collection view of the values contained in this map. | 2.0 |

#### 7.15.17. ReplicatedMap.EntrySet
```
Gets a lazy set view of the mappings contained in this map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d1100

**Partition Identifier:** a random partition ID from `0` to `PARTITION_COUNT`(exclusive)


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |

#### Response Message
**Message Type:** 0x0d1101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | A lazy set view of the mappings contained in this map. | 2.0 |

#### 7.15.18. ReplicatedMap.AddNearCacheEntryListener
```
Adds a near cache entry listener for this map. This listener will be notified when an entry is added/removed/updated/evicted/expired etc. so that the near cache entries can be invalidated.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0d1200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.0 |
| includeValue | boolean | False | True if EntryEvent should contain the value,false otherwise | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x0d1201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | A unique string  which is used as a key to remove the listener. | 2.0 |

#### Event Message

##### Entry
**Message Type:** 0x0d1203

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| key | Data | True | Key of the entry event. | 2.0 |
| value | Data | True | Value of the entry event. | 2.0 |
| oldValue | Data | True | Old value of the entry event. | 2.0 |
| mergingValue | Data | True | Incoming merging value of the entry event. | 2.0 |
| eventType | int | False | Type of the entry event. Possible values are ADDED(1) REMOVED(2) UPDATED(4) EVICTED(8) EXPIRED(16) EVICT_ALL(32) CLEAR_ALL(64) MERGED(128) INVALIDATION(256) LOADED(512) | 2.0 |
| uuid | UUID | False | UUID of the member that dispatches the event. | 2.0 |
| numberOfAffectedEntries | int | False | Number of entries affected by this event. | 2.0 |

#### 7.15.19. ReplicatedMap.PutAllWithMetadata
```
Copies all of the mappings from the specified entry list to this map, including metadata.
This method uses ReplicatedRecordStore.putRecord in the backend.
Please note that all the keys in the request should belong to the partition id to which this request is being sent, all keys
matching to a different partition id shall be ignored. The API implementation using this request may need to send multiple
of these request messages for filling a request for a key set if the keys belong to different partitions.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x0d1300

**Partition Identifier:** Murmur hash of any key belongs to target partition % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of replicated map | 2.7 |
| entries | List of replicatedMapEntryViewHolder | False | entries with metadata | 2.7 |
| partitionId | int | False | partition id of the entries | 2.7 |

#### Response Message
**Message Type:** 0x0d1301

Header only response message, no message body exist.

#### 7.15.20. ReplicatedMap.FetchEntryViews
```
Allows iteration over ReplicatedMapEntryViewHolder objects. The changes happened during the iteration may not be included in the iterated EntryViews. This method
will throw an exception if there is no replicated record store with the given replicated map name and partition id. This method will consume some memory in the 
member with the default timeout of 300 seconds that is reset after each fetch. Sending endEntryViewIteration or timing out will release the resource.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x0d1400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.7 |
| cursorId | UUID | False | The identifier of the last fetched page. Send a random UUID while sending the first fetchEntryViews request to start iteration. Also don't forget to set newIteration to true. Then, use the returned UUIDs in response to feed this parameter and progress iteration. | 2.7 |
| newIteration | boolean | False | Set this true if you are creating a new iteration via fetchEntryViews. fetchEntryViews can also be  used to fetch new pages of an existing iteration. In that case, set this to false.  | 2.7 |
| partitionId | int | False | The partition ID of the partition that the EntryViews belong to. | 2.7 |
| batchSize | int | False | The maximum number of EntryViews to be returned. | 2.7 |

#### Response Message
**Message Type:** 0x0d1401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| cursorId | UUID | False | A UUID which is used to fetch new pages. | 2.7 |
| entryViews | List of replicatedMapEntryViewHolder | False | A list of EntryViews. If the page includes less items than the batchSize, it means the iteration has ended. | 2.7 |

#### 7.15.21. ReplicatedMap.EndEntryViewIteration
```
This method is used to release the resource generated by fetchEntryViews. Send this request after you retrieved the last page and no
longer need the iterator.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x0d1500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the ReplicatedMap | 2.7 |
| cursorId | UUID | True | The identifier of the iterator. This has to be the first cursor id that is returned by fetchEntryViews. | 2.7 |

#### Response Message
**Message Type:** 0x0d1501

Header only response message, no message body exist.

### 7.16. TransactionalMap
**Service id:** 14

#### 7.16.1. TransactionalMap.ContainsKey
```
Returns true if this map contains an entry for the specified key.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The specified key. | 2.0 |

#### Response Message
**Message Type:** 0x0e0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this map contains an entry for the specified key. | 2.0 |

#### 7.16.2. TransactionalMap.Get
```
Returns the value for the specified key, or null if this map does not contain this key.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The specified key | 2.0 |

#### Response Message
**Message Type:** 0x0e0201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The value for the specified key | 2.0 |

#### 7.16.3. TransactionalMap.GetForUpdate
```
Locks the key and then gets and returns the value to which the specified key is mapped. Lock will be released at
the end of the transaction (either commit or rollback).

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The value to which the specified key is mapped | 2.0 |

#### Response Message
**Message Type:** 0x0e0301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The value for the specified key | 2.0 |

#### 7.16.4. TransactionalMap.Size
```
Returns the number of entries in this map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x0e0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of entries in this map. | 2.0 |

#### 7.16.5. TransactionalMap.IsEmpty
```
Returns true if this map contains no entries.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x0e0501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if this map contains no entries. | 2.0 |

#### 7.16.6. TransactionalMap.Put
```
Associates the specified value with the specified key in this map. If the map previously contained a mapping for
the key, the old value is replaced by the specified value. The object to be put will be accessible only in the
current transaction context till transaction is committed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The specified key | 2.0 |
| value | Data | False | The value to associate with the key. | 2.0 |
| ttl | long | False | The duration in milliseconds after which this entry shall be deleted. O means infinite. | 2.0 |

#### Response Message
**Message Type:** 0x0e0601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | Previous value associated with key or  null if there was no mapping for key | 2.0 |

#### 7.16.7. TransactionalMap.Set
```
Associates the specified value with the specified key in this map. If the map previously contained a mapping for
the key, the old value is replaced by the specified value. This method is preferred to #put(Object, Object)
if the old value is not needed.
The object to be set will be accessible only in the current transaction context until the transaction is committed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The specified key | 2.0 |
| value | Data | False | The value to associate with key | 2.0 |

#### Response Message
**Message Type:** 0x0e0701

Header only response message, no message body exist.

#### 7.16.8. TransactionalMap.PutIfAbsent
```
If the specified key is not already associated with a value, associate it with the given value.
The object to be put will be accessible only in the current transaction context until the transaction is committed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The specified key | 2.0 |
| value | Data | False | The value to associate with the key when there is no previous value. | 2.0 |

#### Response Message
**Message Type:** 0x0e0801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The previous value associated with key, or null if there was no mapping for key. | 2.0 |

#### 7.16.9. TransactionalMap.Replace
```
Replaces the entry for a key only if it is currently mapped to some value. The object to be replaced will be
accessible only in the current transaction context until the transaction is committed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The specified key | 2.0 |
| value | Data | False | The value replaced the previous value | 2.0 |

#### Response Message
**Message Type:** 0x0e0901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The previous value associated with key, or null if there was no mapping for key. | 2.0 |

#### 7.16.10. TransactionalMap.ReplaceIfSame
```
Replaces the entry for a key only if currently mapped to a given value. The object to be replaced will be
accessible only in the current transaction context until the transaction is committed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The specified key. | 2.0 |
| oldValue | Data | False | Replace the key value if it is the old value. | 2.0 |
| newValue | Data | False | The new value to replace the old value. | 2.0 |

#### Response Message
**Message Type:** 0x0e0a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the value was replaced. | 2.0 |

#### 7.16.11. TransactionalMap.Remove
```
Removes the mapping for a key from this map if it is present. The map will not contain a mapping for the
specified key once the call returns. The object to be removed will be accessible only in the current transaction
context until the transaction is committed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | Remove the mapping for this key. | 2.0 |

#### Response Message
**Message Type:** 0x0e0b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The previous value associated with key, or null if there was no mapping for key | 2.0 |

#### 7.16.12. TransactionalMap.Delete
```
Removes the mapping for a key from this map if it is present. The map will not contain a mapping for the specified
key once the call returns. This method is preferred to #remove(Object) if the old value is not needed. The object
to be deleted will be removed from only the current transaction context until the transaction is committed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | Remove the mapping for this key. | 2.0 |

#### Response Message
**Message Type:** 0x0e0c01

Header only response message, no message body exist.

#### 7.16.13. TransactionalMap.RemoveIfSame
```
Removes the entry for a key only if currently mapped to a given value. The object to be removed will be removed
from only the current transaction context until the transaction is committed.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The specified key | 2.0 |
| value | Data | False | Remove the key if it has this value. | 2.0 |

#### Response Message
**Message Type:** 0x0e0d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the value was removed | 2.0 |

#### 7.16.14. TransactionalMap.KeySet
```
Returns a set clone of the keys contained in this map. The set is NOT backed by the map, so changes to the map
are NOT reflected in the set, and vice-versa. This method is always executed by a distributed query, so it may throw
a QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x0e0e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | A set clone of the keys contained in this map. | 2.0 |

#### 7.16.15. TransactionalMap.KeySetWithPredicate
```
Queries the map based on the specified predicate and returns the keys of matching entries. Specified predicate
runs on all members in parallel.The set is NOT backed by the map, so changes to the map are NOT reflected in the
set, and vice-versa. This method is always executed by a distributed query, so it may throw a
QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e0f00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| predicate | Data | False | Specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x0e0f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | Result key set for the query. | 2.0 |

#### 7.16.16. TransactionalMap.Values
```
Returns a collection clone of the values contained in this map. The collection is NOT backed by the map,
so changes to the map are NOT reflected in the collection, and vice-versa. This method is always executed by a
distributed query, so it may throw a QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e1000

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x0e1001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | All values in the map | 2.0 |

#### 7.16.17. TransactionalMap.ValuesWithPredicate
```
Queries the map based on the specified predicate and returns the values of matching entries.Specified predicate
runs on all members in parallel. The collection is NOT backed by the map, so changes to the map are NOT reflected
in the collection, and vice-versa. This method is always executed by a distributed query, so it may throw
a QueryResultSizeExceededException if query result size limit is configured.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e1100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| predicate | Data | False | Specified query criteria. | 2.0 |

#### Response Message
**Message Type:** 0x0e1101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | Result value collection of the query. | 2.0 |

#### 7.16.18. TransactionalMap.ContainsValue
```
Returns true if this map contains an entry for the specified value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0e1200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| value | Data | False | The specified value. | 2.0 |

#### Response Message
**Message Type:** 0x0e1201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if this map contains an entry for the specified key. | 2.0 |

### 7.17. TransactionalMultiMap
**Service id:** 15

#### 7.17.1. TransactionalMultiMap.Put
```
Stores a key-value pair in the multimap.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0f0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Multi Map | 2.0 |
| txnId | UUID | False | ID of the transaction | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The key to be stored | 2.0 |
| value | Data | False | The value to be stored | 2.0 |

#### Response Message
**Message Type:** 0x0f0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the size of the multimap is increased, false if the multimap already contains the key-value pair. | 2.0 |

#### 7.17.2. TransactionalMultiMap.Get
```
Returns the collection of values associated with the key.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0f0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Multi Map | 2.0 |
| txnId | UUID | False | ID of the transaction | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The key whose associated values are returned | 2.0 |

#### Response Message
**Message Type:** 0x0f0201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | The collection of the values associated with the key | 2.0 |

#### 7.17.3. TransactionalMultiMap.Remove
```
Removes the given key value pair from the multimap.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0f0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Multi Map | 2.0 |
| txnId | UUID | False | ID of the transaction | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The key whose associated values are returned | 2.0 |

#### Response Message
**Message Type:** 0x0f0301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | True if the size of the multimap changed after the remove operation, false otherwise. | 2.0 |

#### 7.17.4. TransactionalMultiMap.RemoveEntry
```
Removes all the entries associated with the given key.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0f0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Multi Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The key whose associated values are returned | 2.0 |
| value | Data | False | The value to be stored | 2.0 |

#### Response Message
**Message Type:** 0x0f0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the size of the multimap changed after the remove operation, false otherwise. | 2.0 |

#### 7.17.5. TransactionalMultiMap.ValueCount
```
Returns the number of values matching the given key in the multimap.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0f0500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Multi Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| key | Data | False | The key whose number of values are returned | 2.0 |

#### Response Message
**Message Type:** 0x0f0501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of values matching the given key in the multimap | 2.0 |

#### 7.17.6. TransactionalMultiMap.Size
```
Returns the number of key-value pairs in the multimap.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x0f0600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Multi Map | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x0f0601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of key-value pairs in the multimap | 2.0 |

### 7.18. TransactionalSet
**Service id:** 16

#### 7.18.1. TransactionalSet.Add
```
Add new item to transactional set.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x100100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Set | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| item | Data | False | Item added to transactional set | 2.0 |

#### Response Message
**Message Type:** 0x100101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if item is added successfully | 2.0 |

#### 7.18.2. TransactionalSet.Remove
```
Remove item from transactional set.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x100200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Set | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| item | Data | False | Item removed from Transactional Set | 2.0 |

#### Response Message
**Message Type:** 0x100201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if item is remove successfully | 2.0 |

#### 7.18.3. TransactionalSet.Size
```
Returns the size of the set.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x100300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Set | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x100301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The size of the set | 2.0 |

### 7.19. TransactionalList
**Service id:** 17

#### 7.19.1. TransactionalList.Add
```
Adds a new item to the transactional list.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x110100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional List | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| item | Data | False | The new item added to the transactionalList | 2.0 |

#### Response Message
**Message Type:** 0x110101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the item is added successfully, false otherwise | 2.0 |

#### 7.19.2. TransactionalList.Remove
```
Remove item from the transactional list

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x110200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional List | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| item | Data | False | Item to remove to transactional List | 2.0 |

#### Response Message
**Message Type:** 0x110201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the removed successfully,false otherwise | 2.0 |

#### 7.19.3. TransactionalList.Size
```
Returns the size of the list

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x110300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional List | 2.0 |
| txnId | UUID | False | ID of the this transaction operation | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x110301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The size of the list | 2.0 |

### 7.20. TransactionalQueue
**Service id:** 18

#### 7.20.1. TransactionalQueue.Offer
```
Inserts the specified element into this queue, waiting up to the specified wait time if necessary for space to
become available.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x120100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Queue | 2.0 |
| txnId | UUID | False | ID of the transaction | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| item | Data | False | The element to add | 2.0 |
| timeout | long | False | How long to wait before giving up, in milliseconds | 2.0 |

#### Response Message
**Message Type:** 0x120101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | <tt>true</tt> if successful, or <tt>false</tt> if the specified waiting time elapses before space is available | 2.0 |

#### 7.20.2. TransactionalQueue.Take
```
Retrieves and removes the head of this queue, waiting if necessary until an element becomes available.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x120200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Queue | 2.0 |
| txnId | UUID | False | ID of the transaction | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x120201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The head of this queue | 2.0 |

#### 7.20.3. TransactionalQueue.Poll
```
Retrieves and removes the head of this queue, waiting up to the specified wait time if necessary for an element
to become available.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x120300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Queue | 2.0 |
| txnId | UUID | False | ID of the transaction | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| timeout | long | False | How long to wait before giving up, in milliseconds | 2.0 |

#### Response Message
**Message Type:** 0x120301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The head of this queue, or <tt>null</tt> if the specified waiting time elapses before an element is available | 2.0 |

#### 7.20.4. TransactionalQueue.Peek
```
Retrieves, but does not remove, the head of this queue, or returns null if this queue is empty.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x120400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Queue | 2.0 |
| txnId | UUID | False | ID of the transaction | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |
| timeout | long | False | How long to wait before giving up, in milliseconds | 2.0 |

#### Response Message
**Message Type:** 0x120401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The value at the head of the queue. | 2.0 |

#### 7.20.5. TransactionalQueue.Size
```
Returns the number of elements in this collection.If this collection contains more than Integer.MAX_VALUE
elements, returns Integer.MAX_VALUE.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x120500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Transactional Queue | 2.0 |
| txnId | UUID | False | ID of the transaction | 2.0 |
| threadId | long | False | The id of the user thread performing the operation. It is used to guarantee that only the lock holder thread (if a lock exists on the entry) can perform the requested operation. | 2.0 |

#### Response Message
**Message Type:** 0x120501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | The number of elements in this collection | 2.0 |

### 7.21. Cache
**Service id:** 19

#### 7.21.1. Cache.AddEntryListener
```
Adds an entry listener for this cache. For the types of events that the listener
will be notified for, see the documentation of the type field of the Cache event below.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| localOnly | boolean | False | If true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x130101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Registration id for the registered listener. | 2.0 |

#### Event Message

##### Cache
**Message Type:** 0x130103

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| type | int | False | The type of the event. Possible values for the event are: CREATED(1): An event type indicating that the cache entry was created. UPDATED(2): An event type indicating that the cache entry was updated, i.e. a previous mapping existed. REMOVED(3): An event type indicating that the cache entry was removed. EXPIRED(4): An event type indicating that the cache entry has expired. EVICTED(5): An event type indicating that the cache entry has evicted. INVALIDATED(6): An event type indicating that the cache entry has invalidated for near cache invalidation. COMPLETED(7): An event type indicating that the cache operation has completed. EXPIRATION_TIME_UPDATED(8): An event type indicating that the expiration time of cache record has been updated PARTITION_LOST(9): An event type indicating that partition loss is detected in given cache with name | 2.0 |
| keys | List of cacheEventData | False | The keys of the entries in the cache. | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### 7.21.2. Cache.Clear
```
Clears the contents of the cache, without notifying listeners or CacheWriters.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |

#### Response Message
**Message Type:** 0x130201

Header only response message, no message body exist.

#### 7.21.3. Cache.RemoveAllKeys
```
Removes entries for the specified keys. The order in which the individual entries are removed is undefined.
For every entry in the key set, the following are called: any registered CacheEntryRemovedListeners if the cache
is a write-through cache, the CacheWriter. If the key set is empty, the CacheWriter is not called.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| keys | List of data | False | The keys to remove. | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x130301

Header only response message, no message body exist.

#### 7.21.4. Cache.RemoveAll
```
Removes all of the mappings from this cache. The order that the individual entries are removed is undefined.
For every mapping that exists the following are called: any registered CacheEntryRemovedListener if the cache is
a write-through cache, the CacheWriter.If the cache is empty, the CacheWriter is not called.
This is potentially an expensive operation as listeners are invoked. Use  #clear() to avoid this.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x130401

Header only response message, no message body exist.

#### 7.21.5. Cache.ContainsKey
```
Determines if the Cache contains an entry for the specified key. More formally, returns true if and only if this
cache contains a mapping for a key k such that key.equals(k). (There can be at most one such mapping.)

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130500

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | The key whose presence in this cache is to be tested. | 2.0 |

#### Response Message
**Message Type:** 0x130501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | Returns true if cache value for the key exists, false otherwise. | 2.0 |

#### 7.21.6. Cache.CreateConfig
```
Creates the given cache configuration on Hazelcast members.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130600

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| cacheConfig | CacheConfigHolder | False | The cache configuration. | 2.0 |
| createAlsoOnOthers | boolean | False | True if the configuration shall be created on all members, false otherwise. | 2.0 |

#### Response Message
**Message Type:** 0x130601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | CacheConfigHolder | True | The created configuration object. | 2.0 |

#### 7.21.7. Cache.Destroy
```
Closes the cache. Clears the internal content and releases any resource.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130700

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |

#### Response Message
**Message Type:** 0x130701

Header only response message, no message body exist.

#### 7.21.8. Cache.EntryProcessor
```
Applies the user defined EntryProcessor to entry mapped by the key.
Returns the result of the processing, if any, defined by the implementation.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130800

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | the key to the entry | 2.0 |
| entryProcessor | Data | False | Entry processor to invoke. Byte-array which is serialized from an object implementing javax.cache.processor.EntryProcessor. | 2.0 |
| arguments | List of data | False | additional arguments to pass to the EntryProcessor | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x130801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | the result of the processing, if any, defined by the EntryProcessor implementation | 2.0 |

#### 7.21.9. Cache.GetAll
```
Gets a collection of entries from the cache with custom expiry policy, returning them as Map of the values
associated with the set of keys requested. If the cache is configured for read-through operation mode, the underlying
configured javax.cache.integration.CacheLoader might be called to retrieve the values of the keys from any kind
of external resource.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| keys | List of data | False | The keys whose associated values are to be returned. | 2.0 |
| expiryPolicy | Data | True | Expiry policy for the entry. Byte-array which is serialized from an object implementing javax.cache.expiry.ExpiryPolicy interface. | 2.0 |

#### Response Message
**Message Type:** 0x130901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | A map of entries that were found for the given keys. Keys not found in the cache are not in the returned map. | 2.0 |

#### 7.21.10. Cache.GetAndRemove
```
Atomically removes the entry for a key only if currently mapped to some value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130a00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | key with which the specified value is associated | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x130a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | the value if one existed or null if no mapping existed for this key | 2.0 |

#### 7.21.11. Cache.GetAndReplace
```
Atomically replaces the assigned value of the given key by the specified value using a custom
javax.cache.expiry.ExpiryPolicy and returns the previously assigned value. If the cache is configured for
write-through operation mode, the underlying configured javax.cache.integration.CacheWriter might be called to
store the value of the key to any kind of external resource.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130b00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | The key whose value is replaced. | 2.0 |
| value | Data | False | The new value to be associated with the specified key. | 2.0 |
| expiryPolicy | Data | True | Expiry policy for the entry. Byte-array which is serialized from an object implementing javax.cache.expiry.ExpiryPolicy interface. | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x130b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The old value previously assigned to the given key. | 2.0 |

#### 7.21.12. Cache.GetConfig
```
Gets the cache configuration with the given name from members.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130c00

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache with prefix. | 2.0 |
| simpleName | String | False | Name of the cache without prefix. | 2.0 |

#### Response Message
**Message Type:** 0x130c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | CacheConfigHolder | True | The cache configuration. | 2.0 |

#### 7.21.13. Cache.Get
```
Retrieves the mapped value of the given key using a custom javax.cache.expiry.ExpiryPolicy. If no mapping exists
null is returned. If the cache is configured for read-through operation mode, the underlying configured
javax.cache.integration.CacheLoader might be called to retrieve the value of the key from any kind of external resource.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130d00

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | The key whose mapped value is to be returned. | 2.0 |
| expiryPolicy | Data | True | Expiry policy for the entry. Byte-array which is serialized from an object implementing javax.cache.expiry.ExpiryPolicy interface. | 2.0 |

#### Response Message
**Message Type:** 0x130d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The value assigned to the given key, or null if not assigned. | 2.0 |

#### 7.21.14. Cache.Iterate
```
The ordering of iteration over entries is undefined. During iteration, any entries that are a). read will have
their appropriate CacheEntryReadListeners notified and b). removed will have their appropriate
CacheEntryRemoveListeners notified. java.util.Iterator#next() may return null if the entry is no longer present,
has expired or has been evicted.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130e00

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| batch | int | False | The number of items to be batched | 2.0 |

#### Response Message
**Message Type:** 0x130e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| keys | List of data | False | The keys fetched from the cache. | 2.0 |

#### 7.21.15. Cache.ListenerRegistration
```
Tries to register the listener configuration for the cache specified by its name
to the given member.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x130f00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| listenerConfig | Data | False | The listener configuration. Byte-array which is serialized from an object implementing javax.cache.configuration.CacheEntryListenerConfiguration | 2.0 |
| shouldRegister | boolean | False | true if the listener is being registered, false if the listener is being unregistered. | 2.0 |
| uuid | UUID | False | The UUID of the member server for which the listener is being registered for. | 2.0 |

#### Response Message
**Message Type:** 0x130f01

Header only response message, no message body exist.

#### 7.21.16. Cache.LoadAll
```
Loads all the keys into the CacheRecordStore in batch.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131000

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| keys | List of data | False | the keys to load | 2.0 |
| replaceExistingValues | boolean | False | when true existing values in the Cache will be replaced by those loaded from a CacheLoader | 2.0 |

#### Response Message
**Message Type:** 0x131001

Header only response message, no message body exist.

#### 7.21.17. Cache.ManagementConfig
```
Enables or disables the statistics or the management support for the
cache with the given name on a member with the given address.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| isStat | boolean | False | true if enabling statistics, false if enabling management. | 2.0 |
| enabled | boolean | False | true if enabled, false to disable. | 2.0 |
| uuid | UUID | False | the UUID of the host to enable. | 2.0 |

#### Response Message
**Message Type:** 0x131101

Header only response message, no message body exist.

#### 7.21.18. Cache.PutIfAbsent
```
Associates the specified key with the given value if and only if there is not yet a mapping defined for the
specified key. If the cache is configured for write-through operation mode, the underlying configured
javax.cache.integration.CacheWriter might be called to store the value of the key to any kind of external resource.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131200

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | The key that is associated with the specified value. | 2.0 |
| value | Data | False | The value that has the specified key associated with it. | 2.0 |
| expiryPolicy | Data | True | The custom expiry policy for this operation. A null value is equivalent to put(Object, Object). | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x131201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if a value was set, false otherwise. | 2.0 |

#### 7.21.19. Cache.Put
```
Puts the entry with the given key, value and the expiry policy to the cache.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131300

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | The key that has the specified value associated with it. | 2.0 |
| value | Data | False | The value to be associated with the key. | 2.0 |
| expiryPolicy | Data | True | Expiry policy for the entry. Byte-array which is serialized from an object implementing javax.cache.expiry.ExpiryPolicy interface. | 2.0 |
| get | boolean | False | boolean flag indicating if the previous value should be retrieved. | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x131301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The value previously assigned to the given key, or null if not assigned. | 2.0 |

#### 7.21.20. Cache.RemoveEntryListener
```
Removes the specified entry listener. If there is no such listener added before, this call does no change in the
cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| registrationId | UUID | False | The id assigned during the registration for the listener which shall be removed. | 2.0 |

#### Response Message
**Message Type:** 0x131401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the listener is de-registered, false otherwise | 2.0 |

#### 7.21.21. Cache.RemoveInvalidationListener
```
Removes the specified invalidation listener. If there is no such listener added before, this call does no change
in the cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| registrationId | UUID | False | The id assigned during the registration for the listener which shall be removed. | 2.0 |

#### Response Message
**Message Type:** 0x131501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the listener is de-registered, false otherwise | 2.0 |

#### 7.21.22. Cache.Remove
```
Atomically removes the mapping for a key only if currently mapped to the given value.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131600

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | key whose mapping is to be removed from the cache | 2.0 |
| currentValue | Data | True | value expected to be associated with the specified key. | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x131601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | returns false if there was no matching key | 2.0 |

#### 7.21.23. Cache.Replace
```
Atomically replaces the currently assigned value for the given key with the specified newValue if and only if the
currently assigned value equals the value of oldValue using a custom javax.cache.expiry.ExpiryPolicy
If the cache is configured for write-through operation mode, the underlying configured
javax.cache.integration.CacheWriter might be called to store the value of the key to any kind of external resource.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131700

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | False | The key whose value is replaced. | 2.0 |
| oldValue | Data | True | Old value to match if exists before removing. Null means "don't try to remove" | 2.0 |
| newValue | Data | False | The new value to be associated with the specified key. | 2.0 |
| expiryPolicy | Data | True | Expiry policy for the entry. Byte-array which is serialized from an object implementing javax.cache.expiry.ExpiryPolicy interface. | 2.0 |
| completionId | int | False | User generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x131701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The replaced value. | 2.0 |

#### 7.21.24. Cache.Size
```
Total entry count

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |

#### Response Message
**Message Type:** 0x131801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | total entry count | 2.0 |

#### 7.21.25. Cache.AddPartitionLostListener
```
Adds a CachePartitionLostListener. The addPartitionLostListener returns a registration ID. This ID is needed to remove the
CachePartitionLostListener using the #removePartitionLostListener(UUID) method. There is no check for duplicate
registrations, so if you register the listener twice, it will get events twice.Listeners registered from
HazelcastClient may miss some of the cache partition lost events due to design limitations.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache | 2.0 |
| localOnly | boolean | False | if true only node that has the partition sends the request, if false sends all partition lost events. | 2.0 |

#### Response Message
**Message Type:** 0x131901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | returns the registration id for the CachePartitionLostListener. | 2.0 |

#### Event Message

##### CachePartitionLost
**Message Type:** 0x131903

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| partitionId | int | False | Id of the lost partition. | 2.0 |
| uuid | UUID | False | UUID of the member that owns the lost partition. | 2.0 |

#### 7.21.26. Cache.RemovePartitionLostListener
```
Removes the specified cache partition lost listener. If there is no such listener added before, this call does no
change in the cluster and returns false.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Cache | 2.0 |
| registrationId | UUID | False | ID of registered listener. | 2.0 |

#### Response Message
**Message Type:** 0x131a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if registration is removed, false otherwise. | 2.0 |

#### 7.21.27. Cache.PutAll
```
Copies all the mappings from the specified map to this cache with the given expiry policy.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the cache | 2.0 |
| entries | Map of data to data | False | entries to be put as batch | 2.0 |
| expiryPolicy | Data | True | expiry policy for the entry. Byte-array which is serialized from an object implementing {@link javax.cache.expiry.ExpiryPolicy} interface. | 2.0 |
| completionId | int | False | user generated id which shall be received as a field of the cache event upon completion of the request in the cluster. | 2.0 |

#### Response Message
**Message Type:** 0x131b01

Header only response message, no message body exist.

#### 7.21.28. Cache.IterateEntries
```
Fetches specified number of entries from the specified partition starting from specified table index.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131c00

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| batch | int | False | The number of items to be batched | 2.0 |

#### Response Message
**Message Type:** 0x131c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| iterationPointers | Map of integer to integer | False | The index-size pairs that define the state of iteration | 2.0 |
| entries | Map of data to data | False | The entries fetched from the cache. | 2.0 |

#### 7.21.29. Cache.AddNearCacheInvalidationListener
```
Adds listener to cache. This listener will be used to listen near cache invalidation events.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x131d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Registration id for the registered listener. | 2.0 |

#### Event Message

##### CacheInvalidation
**Message Type:** 0x131d03

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| key | Data | True | The key of the invalidated entry. | 2.0 |
| sourceUuid | UUID | True | UUID of the member who fired this event. | 2.0 |
| partitionUuid | UUID | False | UUID of the source partition that invalidated entry belongs to. | 2.0 |
| sequence | long | False | Sequence number of the invalidation event. | 2.0 |

##### CacheBatchInvalidation
**Message Type:** 0x131d04

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the cache. | 2.0 |
| keys | List of data | False | List of the keys of the invalidated entries. | 2.0 |
| sourceUuids | List of uUID | False | List of UUIDs of the members who fired these events. | 2.0 |
| partitionUuids | List of uUID | False | List of UUIDs of the source partitions that invalidated entries belong to. | 2.0 |
| sequences | List of long | False | List of sequence numbers of the invalidation events. | 2.0 |

#### 7.21.30. Cache.FetchNearCacheInvalidationMetadata
```
Fetches invalidation metadata from partitions of map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| names | List of string | False | names of the caches | 2.0 |
| uuid | UUID | False | Address of the member. | 2.0 |

#### Response Message
**Message Type:** 0x131e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| namePartitionSequenceList | Map of string to entryList_Integer_Long | False | Map of partition ids and sequence number of invalidations mapped by the cache name. | 2.0 |
| partitionUuidList | Map of integer to uUID | False | Map of member UUIDs mapped by the partition ids of invalidations. | 2.0 |

#### 7.21.31. Cache.EventJournalSubscribe
```
Performs the initial subscription to the cache event journal.
This includes retrieving the event journal sequences of the
oldest and newest event in the journal.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x131f00

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the cache | 2.0 |

#### Response Message
**Message Type:** 0x131f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| oldestSequence | long | False | Sequence id of the oldest event in the event journal. | 2.0 |
| newestSequence | long | False | Sequence id of the newest event in the event journal. | 2.0 |

#### 7.21.32. Cache.EventJournalRead
```
Reads from the cache event journal in batches. You may specify the start sequence,
the minimum required number of items in the response, the maximum number of items
in the response, a predicate that the events should pass and a projection to
apply to the events in the journal.
If the event journal currently contains less events than {@code minSize}, the
call will wait until it has sufficient items.
The predicate, filter and projection may be {@code null} in which case all elements are returned
and no projection is applied.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x132000

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the cache | 2.0 |
| startSequence | long | False | the startSequence of the first item to read | 2.0 |
| minSize | int | False | the minimum number of items to read. | 2.0 |
| maxSize | int | False | the maximum number of items to read. | 2.0 |
| predicate | Data | True | the predicate to apply before processing events | 2.0 |
| projection | Data | True | the projection to apply to journal events | 2.0 |

#### Response Message
**Message Type:** 0x132001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| readCount | int | False | Number of items that have been read. | 2.0 |
| items | List of data | False | List of items that have been read. | 2.0 |
| itemSeqs | longArray | True | Sequence numbers of items in the event journal. | 2.0 |
| nextSeq | long | False | Sequence number of the item following the last read item. | 2.0 |

#### 7.21.33. Cache.SetExpiryPolicy
```
Associates the specified key with the given {@link javax.cache.expiry.ExpiryPolicy}.
{@code expiryPolicy} takes precedence for these particular {@code keys} against any cache wide expiry policy.
If some keys in {@code keys} do not exist or are already expired, this call has no effect for those.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x132100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the cache | 2.0 |
| keys | List of data | False | The keys that are associated with the specified expiry policy. | 2.0 |
| expiryPolicy | Data | False | custom expiry policy for this operation | 2.0 |

#### Response Message
**Message Type:** 0x132101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | { | 2.0 |

### 7.22. XATransaction
**Service id:** 20

#### 7.22.1. XATransaction.ClearRemote
```
Clears the XA transaction with the given xid from remote member.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x140100

**Partition Identifier:** Murmur hash of xid % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| xid | Xid | False | Java XA transaction id as defined in interface javax.transaction.xa.Xid. | 2.0 |

#### Response Message
**Message Type:** 0x140101

Header only response message, no message body exist.

#### 7.22.2. XATransaction.CollectTransactions
```
Obtains a list of prepared transaction from the cluster.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x140200

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0x140201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of xid | False | Array of Xids. | 2.0 |

#### 7.22.3. XATransaction.Finalize
```
Finalizes the commit of XA transaction with the given xid.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x140300

**Partition Identifier:** Murmur hash of xid % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| xid | Xid | False | Java XA transaction id as defined in interface javax.transaction.xa.Xid. | 2.0 |
| isCommit | boolean | False | If true, the transaction is committed else transaction is rolled back. | 2.0 |

#### Response Message
**Message Type:** 0x140301

Header only response message, no message body exist.

#### 7.22.4. XATransaction.Commit
```
Commits the global transaction specified by xid.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x140400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| transactionId | UUID | False | The internal Hazelcast transaction id. | 2.0 |
| onePhase | boolean | False | If true, the prepare is also done. | 2.0 |

#### Response Message
**Message Type:** 0x140401

Header only response message, no message body exist.

#### 7.22.5. XATransaction.Create
```
Creates an XA transaction with the given parameters.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x140500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| xid | Xid | False | Java XA transaction id as defined in interface javax.transaction.xa.Xid. | 2.0 |
| timeout | long | False | The timeout in seconds for XA operations such as prepare, commit, rollback. | 2.0 |

#### Response Message
**Message Type:** 0x140501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | The transaction unique identifier. | 2.0 |

#### 7.22.6. XATransaction.Prepare
```
Ask a member to prepare for a transaction commit of the transaction specified in xid.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x140600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| transactionId | UUID | False | The id of the transaction to prepare. | 2.0 |

#### Response Message
**Message Type:** 0x140601

Header only response message, no message body exist.

#### 7.22.7. XATransaction.Rollback
```
Informs the member to roll back work done on behalf of a transaction.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x140700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| transactionId | UUID | False | The id of the transaction to rollback. | 2.0 |

#### Response Message
**Message Type:** 0x140701

Header only response message, no message body exist.

### 7.23. Transaction
**Service id:** 21

#### 7.23.1. Transaction.Commit
```
Commits the transaction with the given id.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x150100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| transactionId | UUID | False | The internal Hazelcast transaction id. | 2.0 |
| threadId | long | False | The thread id for the transaction. | 2.0 |

#### Response Message
**Message Type:** 0x150101

Header only response message, no message body exist.

#### 7.23.2. Transaction.Create
```
Creates a transaction with the given parameters.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x150200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| timeout | long | False | The maximum allowed duration for the transaction operations. | 2.0 |
| durability | int | False | The durability of the transaction | 2.0 |
| transactionType | int | False | Identifies the type of the transaction. Possible values are: 1 (Two phase):  The two phase commit is more than the classic two phase commit (if you want a regular two phase commit, use local). Before it commits, it copies the commit-log to other members, so in case of member failure, another member can complete the commit. 2 (Local): Unlike the name suggests, local is a two phase commit. So first all cohorts are asked to prepare if everyone agrees then all cohorts are asked to commit. The problem happens when during the commit phase one or more members crash, that the system could be left in an inconsistent state. | 2.0 |
| threadId | long | False | The thread id for the transaction. | 2.0 |

#### Response Message
**Message Type:** 0x150201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | The transaction id for the created transaction. | 2.0 |

#### 7.23.3. Transaction.Rollback
```
Rollbacks the transaction with the given id.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x150300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| transactionId | UUID | False | The internal Hazelcast transaction id. | 2.0 |
| threadId | long | False | The thread id for the transaction. | 2.0 |

#### Response Message
**Message Type:** 0x150301

Header only response message, no message body exist.

### 7.24. ContinuousQuery
**Service id:** 22

#### 7.24.1. ContinuousQuery.PublisherCreateWithValue
```
Creates a publisher that includes value for the cache events it sends.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x160100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| mapName | String | False | Name of the map. | 2.0 |
| cacheName | String | False | Name of the cache for query cache. | 2.0 |
| predicate | Data | False | The predicate to filter events which will be applied to the QueryCache. | 2.0 |
| batchSize | int | False | The size of batch. After reaching this minimum size, node immediately sends buffered events to QueryCache. | 2.0 |
| bufferSize | int | False | Maximum number of events which can be stored in a buffer of partition. | 2.0 |
| delaySeconds | long | False | The minimum number of delay seconds which an event waits in the buffer of node. | 2.0 |
| populate | boolean | False | Flag to enable/disable initial population of the QueryCache. | 2.0 |
| coalesce | boolean | False | Flag to enable/disable coalescing. If true, then only the last updated value for a key is placed in the batch, otherwise all changed values are included in the update. | 2.0 |

#### Response Message
**Message Type:** 0x160101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Map of data to data | False | Array of key-value pairs. | 2.0 |

#### 7.24.2. ContinuousQuery.PublisherCreate
```
Creates a publisher that does not include value for the cache events it sends.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x160200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| mapName | String | False | Name of the map. | 2.0 |
| cacheName | String | False | Name of query cache. | 2.0 |
| predicate | Data | False | The predicate to filter events which will be applied to the QueryCache. | 2.0 |
| batchSize | int | False | The size of batch. After reaching this minimum size, node immediately sends buffered events to QueryCache. | 2.0 |
| bufferSize | int | False | Maximum number of events which can be stored in a buffer of partition. | 2.0 |
| delaySeconds | long | False | The minimum number of delay seconds which an event waits in the buffer of node. | 2.0 |
| populate | boolean | False | Flag to enable/disable initial population of the QueryCache. | 2.0 |
| coalesce | boolean | False | Flag to enable/disable coalescing. If true, then only the last updated value for a key is placed in the batch, otherwise all changed values are included in the update. | 2.0 |

#### Response Message
**Message Type:** 0x160201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of data | False | Array of keys. | 2.0 |

#### 7.24.3. ContinuousQuery.MadePublishable
```
Makes the query cache with the given name for a specific map publishable.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x160300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| mapName | String | False | Name of the map. | 2.0 |
| cacheName | String | False | Name of query cache. | 2.0 |

#### Response Message
**Message Type:** 0x160301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if successfully set as publishable, false otherwise. | 2.0 |

#### 7.24.4. ContinuousQuery.AddListener
```
Adds a listener to be notified for the events fired on the underlying map on all nodes.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x160400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| listenerName | String | False | Name of the MapListener which will be used to listen this QueryCache | 2.0 |
| localOnly | boolean | False | if true fires events that originated from this node only, otherwise fires all events | 2.0 |

#### Response Message
**Message Type:** 0x160401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Registration id for the listener. | 2.0 |

#### Event Message

##### QueryCacheSingle
**Message Type:** 0x160403

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| data | QueryCacheEventData | False | Data that holds the details of the event such as key, value, old value, new value and creation time. | 2.0 |

##### QueryCacheBatch
**Message Type:** 0x160404

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| events | List of queryCacheEventData | False | List of events in the form of data that holds the details of the event such as key, value, old value, new value and creation time. | 2.0 |
| source | String | False | Source that dispatches this batch event. | 2.0 |
| partitionId | int | False | Id of the partition that holds the keys of the batch event. | 2.0 |

#### 7.24.5. ContinuousQuery.SetReadCursor
```
This method can be used to recover from a possible event loss situation.
This method tries to make consistent the data in this `QueryCache` with the data in the underlying `IMap`
by replaying the events after last consistently received ones. As a result of this replaying logic, same event may
appear more than once to the `QueryCache` listeners.
This method returns `false` if the event is not in the buffer of event publisher side. That means recovery is not
possible.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x160500

**Partition Identifier:** Murmur hash of associated key with sequence % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| mapName | String | False | Name of the map. | 2.0 |
| cacheName | String | False | Name of query cache. | 2.0 |
| sequence | long | False | The cursor position of the accumulator to be set. | 2.0 |

#### Response Message
**Message Type:** 0x160501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the cursor position could be set, false otherwise. | 2.0 |

#### 7.24.6. ContinuousQuery.DestroyCache
```
Destroys the query cache with the given name for a specific map.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x160600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| mapName | String | False | Name of the map. | 2.0 |
| cacheName | String | False | Name of query cache. | 2.0 |

#### Response Message
**Message Type:** 0x160601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if all cache is destroyed, false otherwise. | 2.0 |

### 7.25. Ringbuffer
**Service id:** 23

#### 7.25.1. Ringbuffer.Size
```
Returns number of items in the ringbuffer. If no ttl is set, the size will always be equal to capacity after the
head completed the first looparound the ring. This is because no items are getting retired.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170100

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |

#### Response Message
**Message Type:** 0x170101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the size | 2.0 |

#### 7.25.2. Ringbuffer.TailSequence
```
Returns the sequence of the tail. The tail is the side of the ringbuffer where the items are added to.
The initial value of the tail is -1.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170200

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |

#### Response Message
**Message Type:** 0x170201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the sequence of the tail | 2.0 |

#### 7.25.3. Ringbuffer.HeadSequence
```
Returns the sequence of the head. The head is the side of the ringbuffer where the oldest items in the ringbuffer
are found. If the RingBuffer is empty, the head will be one more than the tail.
The initial value of the head is 0 (1 more than tail).

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170300

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |

#### Response Message
**Message Type:** 0x170301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the sequence of the head | 2.0 |

#### 7.25.4. Ringbuffer.Capacity
```
Returns the capacity of this Ringbuffer.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170400

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |

#### Response Message
**Message Type:** 0x170401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the capacity | 2.0 |

#### 7.25.5. Ringbuffer.RemainingCapacity
```
Returns the remaining capacity of the ringbuffer. The returned value could be stale as soon as it is returned.
If ttl is not set, the remaining capacity will always be the capacity.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170500

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |

#### Response Message
**Message Type:** 0x170501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the remaining capacity | 2.0 |

#### 7.25.6. Ringbuffer.Add
```
Adds an item to the tail of the Ringbuffer. If there is space in the ringbuffer, the call
will return the sequence of the written item. If there is no space, it depends on the overflow policy what happens:
OverflowPolicy OVERWRITE we just overwrite the oldest item in the ringbuffer and we violate the ttl
OverflowPolicy FAIL we return -1. The reason that FAIL exist is to give the opportunity to obey the ttl.
<p/>
This sequence will always be unique for this Ringbuffer instance so it can be used as a unique id generator if you are
publishing items on this Ringbuffer. However you need to take care of correctly determining an initial id when any node
uses the ringbuffer for the first time. The most reliable way to do that is to write a dummy item into the ringbuffer and
use the returned sequence as initial  id. On the reading side, this dummy item should be discard. Please keep in mind that
this id is not the sequence of the item you are about to publish but from a previously published item. So it can't be used
to find that item.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170600

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |
| overflowPolicy | int | False | the OverflowPolicy to use. | 2.0 |
| value | Data | False | to item to add | 2.0 |

#### Response Message
**Message Type:** 0x170601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the sequence of the added item, or -1 if the add failed. | 2.0 |

#### 7.25.7. Ringbuffer.ReadOne
```
Reads one item from the Ringbuffer. If the sequence is one beyond the current tail, this call blocks until an
item is added. This method is not destructive unlike e.g. a queue.take. So the same item can be read by multiple
readers or it can be read multiple times by the same reader. Currently it isn't possible to control how long this
call is going to block. In the future we could add e.g. tryReadOne(long sequence, long timeout, TimeUnit unit).

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170700

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |
| sequence | long | False | the sequence of the item to read. | 2.0 |

#### Response Message
**Message Type:** 0x170701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | the read item | 2.0 |

#### 7.25.8. Ringbuffer.AddAll
```
Adds all the items of a collection to the tail of the Ringbuffer. A addAll is likely to outperform multiple calls
to add(Object) due to better io utilization and a reduced number of executed operations. If the batch is empty,
the call is ignored. When the collection is not empty, the content is copied into a different data-structure.
This means that: after this call completes, the collection can be re-used. the collection doesn't need to be serializable.
If the collection is larger than the capacity of the ringbuffer, then the items that were written first will be
overwritten. Therefor this call will not block. The items are inserted in the order of the Iterator of the collection.
If an addAll is executed concurrently with an add or addAll, no guarantee is given that items are contiguous.
The result of the future contains the sequenceId of the last written item

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170800

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |
| valueList | List of data | False | the batch of items to add | 2.0 |
| overflowPolicy | int | False | the overflowPolicy to use | 2.0 |

#### Response Message
**Message Type:** 0x170801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the CompletionStage to synchronize on completion. | 2.0 |

#### 7.25.9. Ringbuffer.ReadMany
```
Reads a batch of items from the Ringbuffer. If the number of available items after the first read item is smaller
than the maxCount, these items are returned. So it could be the number of items read is smaller than the maxCount.
If there are less items available than minCount, then this call blacks. Reading a batch of items is likely to
perform better because less overhead is involved. A filter can be provided to only select items that need to be read.
If the filter is null, all items are read. If the filter is not null, only items where the filter function returns
true are returned. Using filters is a good way to prevent getting items that are of no value to the receiver.
This reduces the amount of IO and the number of operations being executed, and can result in a significant performance improvement.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x170900

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Ringbuffer | 2.0 |
| startSequence | long | False | the startSequence of the first item to read | 2.0 |
| minCount | int | False | the minimum number of items to read. | 2.0 |
| maxCount | int | False | the maximum number of items to read. | 2.0 |
| filter | Data | True | Filter is allowed to be null, indicating there is no filter. | 2.0 |

#### Response Message
**Message Type:** 0x170901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| readCount | int | False | Number of items that have been read before filtering. | 2.0 |
| items | List of data | False | List of items that have been read. | 2.0 |
| itemSeqs | longArray | True | List of sequence numbers for the items that have been read. | 2.0 |
| nextSeq | long | False | Sequence number of the item following the last read item. | 2.0 |

### 7.26. DurableExecutor
**Service id:** 24

#### 7.26.1. DurableExecutor.Shutdown
```
Initiates an orderly shutdown in which previously submitted tasks are executed, but no new tasks will be accepted.
Invocation has no additional effect if already shut down.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x180100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |

#### Response Message
**Message Type:** 0x180101

Header only response message, no message body exist.

#### 7.26.2. DurableExecutor.IsShutdown
```
Returns true if this executor has been shut down.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x180200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |

#### Response Message
**Message Type:** 0x180201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if this executor has been shut down | 2.0 |

#### 7.26.3. DurableExecutor.SubmitToPartition
```
Submits the task to partition for execution

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x180300

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |
| callable | Data | False | The callable object to be executed. | 2.0 |

#### Response Message
**Message Type:** 0x180301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | the sequence for the submitted execution. | 2.0 |

#### 7.26.4. DurableExecutor.RetrieveResult
```
Retrieves the result of the execution with the given sequence

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x180400

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |
| sequence | int | False | Sequence of the execution. | 2.0 |

#### Response Message
**Message Type:** 0x180401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the callable execution with the given sequence. | 2.0 |

#### 7.26.5. DurableExecutor.DisposeResult
```
Disposes the result of the execution with the given sequence

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x180500

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |
| sequence | int | False | Sequence of the execution. | 2.0 |

#### Response Message
**Message Type:** 0x180501

Header only response message, no message body exist.

#### 7.26.6. DurableExecutor.RetrieveAndDisposeResult
```
Retrieves and disposes the result of the execution with the given sequence

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x180600

**Partition Identifier:** the value passed in to the `partitionId` parameter


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the executor. | 2.0 |
| sequence | int | False | Sequence of the execution. | 2.0 |

#### Response Message
**Message Type:** 0x180601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the callable execution with the given sequence. | 2.0 |

### 7.27. CardinalityEstimator
**Service id:** 25

#### 7.27.1. CardinalityEstimator.Add
```
Add a new hash in the estimation set. This is the method you want to
use to feed hash values into the estimator.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x190100

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | The name of CardinalityEstimator | 2.0 |
| hash | long | False | 64bit hash code value to add  @since 1.3 | 2.0 |

#### Response Message
**Message Type:** 0x190101

Header only response message, no message body exist.

#### 7.27.2. CardinalityEstimator.Estimate
```
Estimates the cardinality of the aggregation so far.
If it was previously estimated and never invalidated, then the cached version is used.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x190200

**Partition Identifier:** Murmur hash of name % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | The name of CardinalityEstimator | 2.0 |

#### Response Message
**Message Type:** 0x190201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the previous cached estimation or the newly computed one. | 2.0 |

### 7.28. ScheduledExecutor
**Service id:** 26

#### 7.28.1. ScheduledExecutor.Shutdown
```
Initiates an orderly shutdown in which previously submitted tasks are executed, but no new tasks will be accepted.
Invocation has no additional effect if already shut down.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | Name of the scheduler. | 2.0 |
| memberUuid | UUID | False | The UUID of the member where the shutdown for this scheduler will be sent. | 2.0 |

#### Response Message
**Message Type:** 0x1a0101

Header only response message, no message body exist.

#### 7.28.2. ScheduledExecutor.SubmitToPartition
```
Submits the task to partition for execution, partition is chosen based on multiple criteria of the given task.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0200

**Partition Identifier:** Murmur hash of taskName % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| type | byte | False | type of schedule logic, values 0 for SINGLE_RUN, 1 for AT_FIXED_RATE | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| task | Data | False | Name The name of the task | 2.0 |
| initialDelayInMillis | long | False | initial delay in milliseconds | 2.0 |
| periodInMillis | long | False | period between each run in milliseconds | 2.0 |
| autoDisposable | boolean | False | A boolean flag to indicate whether the task should be destroyed automatically after execution. | 2.1 |

#### Response Message
**Message Type:** 0x1a0201

Header only response message, no message body exist.

#### 7.28.3. ScheduledExecutor.SubmitToMember
```
Submits the task to a member for execution. Member is provided with its uuid.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| memberUuid | UUID | False | The UUID of the member where the task will get scheduled. | 2.0 |
| type | byte | False | type of schedule logic, values 0 for SINGLE_RUN, 1 for AT_FIXED_RATE | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| task | Data | False | Name The name of the task | 2.0 |
| initialDelayInMillis | long | False | initial delay in milliseconds | 2.0 |
| periodInMillis | long | False | period between each run in milliseconds | 2.0 |
| autoDisposable | boolean | False | A boolean flag to indicate whether the task should be destroyed automatically after execution. | 2.1 |

#### Response Message
**Message Type:** 0x1a0301

Header only response message, no message body exist.

#### 7.28.4. ScheduledExecutor.GetAllScheduledFutures
```
Returns all scheduled tasks in for a given scheduler in the given member.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |

#### Response Message
**Message Type:** 0x1a0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| handlers | List of scheduledTaskHandler | False | A list of scheduled task handlers used to construct the future proxies. | 2.0 |

#### 7.28.5. ScheduledExecutor.GetStatsFromPartition
```
Returns statistics of the task

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0500

**Partition Identifier:** Murmur hash of taskName % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |

#### Response Message
**Message Type:** 0x1a0501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| lastIdleTimeNanos | long | False | Last period of time the task was idle, waiting to get scheduled. | 2.0 |
| totalIdleTimeNanos | long | False | Total amount of time the task was idle, waiting to get scheduled in. | 2.0 |
| totalRuns | long | False | How many times the task was ran/called. | 2.0 |
| totalRunTimeNanos | long | False | The total amount of time the task spent while scheduled in. | 2.0 |
| lastRunDurationNanos | long | False | The duration of the task's last execution. | 2.0 |

#### 7.28.6. ScheduledExecutor.GetStatsFromMember
```
Returns statistics of the task

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| memberUuid | UUID | False | The UUID of the member where the task will get scheduled. | 2.0 |

#### Response Message
**Message Type:** 0x1a0601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| lastIdleTimeNanos | long | False | Last period of time the task was idle, waiting to get scheduled. | 2.0 |
| totalIdleTimeNanos | long | False | Total amount of time the task was idle, waiting to get scheduled in. | 2.0 |
| totalRuns | long | False | How many times the task was ran/called. | 2.0 |
| totalRunTimeNanos | long | False | The total amount of time the task spent while scheduled in. | 2.0 |
| lastRunDurationNanos | long | False | The duration of the task's last execution. | 2.0 |

#### 7.28.7. ScheduledExecutor.GetDelayFromPartition
```
Returns the ScheduledFuture's delay in nanoseconds for the task in the scheduler.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0700

**Partition Identifier:** Murmur hash of taskName % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |

#### Response Message
**Message Type:** 0x1a0701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | The remaining delay of the task formatted in nanoseconds. | 2.0 |

#### 7.28.8. ScheduledExecutor.GetDelayFromMember
```
Returns the ScheduledFuture's delay in nanoseconds for the task in the scheduler.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| memberUuid | UUID | False | The UUID of the member where the task will get scheduled. | 2.0 |

#### Response Message
**Message Type:** 0x1a0801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | The remaining delay of the task formatted in nanoseconds. | 2.0 |

#### 7.28.9. ScheduledExecutor.CancelFromPartition
```
Cancels further execution and scheduling of the task

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0900

**Partition Identifier:** Murmur hash of taskName % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| mayInterruptIfRunning | boolean | False | A boolean flag to indicate whether the task should be interrupted. | 2.0 |

#### Response Message
**Message Type:** 0x1a0901

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the task was cancelled | 2.0 |

#### 7.28.10. ScheduledExecutor.CancelFromMember
```
Cancels further execution and scheduling of the task

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| memberUuid | UUID | False | The UUID of the member where the task will get scheduled. | 2.0 |
| mayInterruptIfRunning | boolean | False | A boolean flag to indicate whether the task should be interrupted. | 2.0 |

#### Response Message
**Message Type:** 0x1a0a01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the task was cancelled | 2.0 |

#### 7.28.11. ScheduledExecutor.IsCancelledFromPartition
```
Checks whether a task as identified from the given handler is already cancelled.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0b00

**Partition Identifier:** Murmur hash of taskName % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |

#### Response Message
**Message Type:** 0x1a0b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the task is cancelled | 2.0 |

#### 7.28.12. ScheduledExecutor.IsCancelledFromMember
```
Checks whether a task as identified from the given handler is already cancelled.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| memberUuid | UUID | False | The UUID of the member where the task will get scheduled. | 2.0 |

#### Response Message
**Message Type:** 0x1a0c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the task is cancelled | 2.0 |

#### 7.28.13. ScheduledExecutor.IsDoneFromPartition
```
Checks whether a task is done.
@see {@link java.util.concurrent.Future#cancel(boolean)}

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0d00

**Partition Identifier:** Murmur hash of taskName % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |

#### Response Message
**Message Type:** 0x1a0d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the task is done | 2.0 |

#### 7.28.14. ScheduledExecutor.IsDoneFromMember
```
Checks whether a task is done.
@see {@link java.util.concurrent.Future#cancel(boolean)}

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| memberUuid | UUID | False | The UUID of the member where the task will get scheduled. | 2.0 |

#### Response Message
**Message Type:** 0x1a0e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if the task is done | 2.0 |

#### 7.28.15. ScheduledExecutor.GetResultFromPartition
```
Fetches the result of the task ({@link java.util.concurrent.Callable})
The call will blocking until the result is ready.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a0f00

**Partition Identifier:** Murmur hash of taskName % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |

#### Response Message
**Message Type:** 0x1a0f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the completed task, in serialized form ({ | 2.0 |

#### 7.28.16. ScheduledExecutor.GetResultFromMember
```
Fetches the result of the task ({@link java.util.concurrent.Callable})
The call will blocking until the result is ready.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a1000

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| memberUuid | UUID | False | The uuid of the member where the task will get scheduled. | 2.0 |

#### Response Message
**Message Type:** 0x1a1001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the completed task, in serialized form ({ | 2.0 |

#### 7.28.17. ScheduledExecutor.DisposeFromPartition
```
Dispose the task from the scheduler

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a1100

**Partition Identifier:** Murmur hash of taskName % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |

#### Response Message
**Message Type:** 0x1a1101

Header only response message, no message body exist.

#### 7.28.18. ScheduledExecutor.DisposeFromMember
```
Dispose the task from the scheduler

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1a1200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| schedulerName | String | False | The name of the scheduler. | 2.0 |
| taskName | String | False | The name of the task | 2.0 |
| memberUuid | UUID | False | The UUID of the member where the task will get scheduled. | 2.0 |

#### Response Message
**Message Type:** 0x1a1201

Header only response message, no message body exist.

### 7.29. DynamicConfig
**Service id:** 27

#### 7.29.1. DynamicConfig.AddMultiMapConfig
```
Adds a new multimap config to a running cluster.
If a multimap configuration with the given {@code name} already exists, then
the new multimap config is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | multimap configuration name | 2.0 |
| collectionType | String | False | value collection type. Valid values are SET and LIST. | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | entry listener configurations | 2.0 |
| binary | boolean | False | {@code true} to store values in {@code BINARY} format or {@code false} to store values in {@code OBJECT} format. | 2.0 |
| backupCount | int | False | number of synchronous backups | 2.0 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.0 |
| statisticsEnabled | boolean | False | set to {@code true} to enable statistics on this multimap configuration | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| mergePolicy | String | False | Name of a class implementing SplitBrainMergePolicy that handles merging of values for this cache while recovering from network partitioning. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.0 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0101

Header only response message, no message body exist.

#### 7.29.2. DynamicConfig.AddRingbufferConfig
```
Adds a new ringbuffer configuration to a running cluster.
If a ringbuffer configuration with the given {@code name} already exists, then
the new ringbuffer config is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | ringbuffer configuration name | 2.0 |
| capacity | int | False | capacity of the ringbuffer | 2.0 |
| backupCount | int | False | number of synchronous backups | 2.0 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.0 |
| timeToLiveSeconds | int | False | maximum number of seconds for each entry to stay in the ringbuffer | 2.0 |
| inMemoryFormat | String | False | in memory format of items in the ringbuffer. Valid options are {@code BINARY} and {@code OBJECT} | 2.0 |
| ringbufferStoreConfig | RingbufferStoreConfigHolder | True | backing ringbuffer store configuration | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| mergePolicy | String | False | Name of a class implementing SplitBrainMergePolicy that handles merging of values for this cache while recovering from network partitioning. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.0 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0201

Header only response message, no message body exist.

#### 7.29.3. DynamicConfig.AddCardinalityEstimatorConfig
```
Adds a new cardinality estimator configuration to a running cluster.
If a cardinality estimator configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the cardinality estimator configuration | 2.0 |
| backupCount | int | False | number of synchronous backups | 2.0 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| mergePolicy | String | False | Name of a class implementing SplitBrainMergePolicy that handles merging of values for this cache while recovering from network partitioning. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.0 |

#### Response Message
**Message Type:** 0x1b0301

Header only response message, no message body exist.

#### 7.29.4. DynamicConfig.AddListConfig
```
Adds a new list configuration to a running cluster.
If a list configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | list's name | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | item listener configurations | 2.0 |
| backupCount | int | False | number of synchronous backups | 2.0 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.0 |
| maxSize | int | False | maximum size of the list | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics on the list, otherwise {@code false} | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| mergePolicy | String | False | Name of a class implementing SplitBrainMergePolicy that handles merging of values for this cache while recovering from network partitioning. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.0 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0401

Header only response message, no message body exist.

#### 7.29.5. DynamicConfig.AddSetConfig
```
Adds a new set configuration to a running cluster.
If a set configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | set's name | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | item listener configurations | 2.0 |
| backupCount | int | False | number of synchronous backups | 2.0 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.0 |
| maxSize | int | False | maximum size of the set | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics on the list, otherwise {@code false} | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| mergePolicy | String | False | Name of a class implementing SplitBrainMergePolicy that handles merging of values for this cache while recovering from network partitioning. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.0 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0501

Header only response message, no message body exist.

#### 7.29.6. DynamicConfig.AddReplicatedMapConfig
```
Adds a new replicated map configuration to a running cluster.
If a replicated map configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the replicated map configuration | 2.0 |
| inMemoryFormat | String | False | data type used to store entries. Valid values are {@code "BINARY"}, {@code "OBJECT"} and {@code "NATIVE"}. | 2.0 |
| asyncFillup | boolean | False | {@code true} to make the replicated map available for reads before initial replication is completed, {@code false} otherwise. | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.0 |
| mergePolicy | String | False | class name of a class implementing SplitBrainMergePolicy to merge entries while recovering from a split brain | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | entry listener configurations | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.0 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0601

Header only response message, no message body exist.

#### 7.29.7. DynamicConfig.AddTopicConfig
```
Adds a new topic configuration to a running cluster.
If a topic configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | topic's name | 2.0 |
| globalOrderingEnabled | boolean | False | when {@code true} all nodes listening to the same topic get their messages in the same order | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.0 |
| multiThreadingEnabled | boolean | False | {@code true} to enable multi-threaded processing of incoming messages, otherwise a single thread will handle all topic messages | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | message listener configurations | 2.0 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0701

Header only response message, no message body exist.

#### 7.29.8. DynamicConfig.AddExecutorConfig
```
Adds a new executor configuration to a running cluster.
If an executor configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | executor's name | 2.0 |
| poolSize | int | False | executor thread pool size | 2.0 |
| queueCapacity | int | False | capacity of executor queue. A value of {@code 0} implies {@link Integer#MAX_VALUE} | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0801

Header only response message, no message body exist.

#### 7.29.9. DynamicConfig.AddDurableExecutorConfig
```
Adds a new durable executor configuration to a running cluster.
If a durable executor configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | durable executor name | 2.0 |
| poolSize | int | False | executor thread pool size | 2.0 |
| durability | int | False | executor's durability | 2.0 |
| capacity | int | False | capacity of executor tasks per partition | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.1 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0901

Header only response message, no message body exist.

#### 7.29.10. DynamicConfig.AddScheduledExecutorConfig
```
Adds a new scheduled executor configuration to a running cluster.
If a scheduled executor configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of scheduled executor | 2.0 |
| poolSize | int | False | number of executor threads per member for the executor | 2.0 |
| durability | int | False | durability of the scheduled executor | 2.0 |
| capacity | int | False | maximum number of tasks that a scheduler can have at any given point in time per partition or per node according to the capacity policy | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |
| mergePolicy | String | False | Name of a class implementing SplitBrainMergePolicy that handles merging of values for this cache while recovering from network partitioning. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.1 |
| capacityPolicy | byte | False | Capacity policy for the configured capacity value | 2.5 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0a01

Header only response message, no message body exist.

#### 7.29.11. DynamicConfig.AddQueueConfig
```
Adds a new queue configuration to a running cluster.
If a queue configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0b00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | queue name | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | item listeners configuration | 2.0 |
| backupCount | int | False | number of synchronous backups | 2.0 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.0 |
| maxSize | int | False | maximum number of items in the queue | 2.0 |
| emptyQueueTtl | int | False | queue time-to-live in seconds: queue will be destroyed if it stays empty or unused for that time | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the queue to remain functional. When {@code null}, split brain protection does not apply to this queue configuration's operations. | 2.0 |
| queueStoreConfig | QueueStoreConfigHolder | True | backing queue store configuration | 2.0 |
| mergePolicy | String | False | Classname of the merge policy. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.0 |
| priorityComparatorClassName | String | True | Class name of the configured {@link java.util.Comparator} implementation. | 2.1 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0b01

Header only response message, no message body exist.

#### 7.29.12. DynamicConfig.AddMapConfig
```
Adds a new map configuration to a running cluster.
If a map configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the map | 2.0 |
| backupCount | int | False | number of synchronous backups | 2.0 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.0 |
| timeToLiveSeconds | int | False | maximum number of seconds for each entry to stay in the map. | 2.0 |
| maxIdleSeconds | int | False | maximum number of seconds for each entry to stay idle in the map | 2.0 |
| evictionConfig | EvictionConfigHolder | True | map eviction configuration | 2.0 |
| readBackupData | boolean | False | {@code true} to enable reading local backup entries, {@code false} otherwise | 2.0 |
| cacheDeserializedValues | String | False | control caching of de-serialized values. Valid values are {@code NEVER} (Never cache de-serialized object), {@code INDEX_ONLY} (Cache values only when they are inserted into an index) and {@code ALWAYS} (Always cache de-serialized values | 2.0 |
| mergePolicy | String | False | Name of a class implementing SplitBrainMergePolicy that handles merging of values for this cache while recovering from network partitioning. | 2.0 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation | 2.0 |
| inMemoryFormat | String | False | data type used to store entries. Valid values are {@code BINARY}, {@code OBJECT} and {@code NATIVE}. | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | entry listener configurations | 2.0 |
| partitionLostListenerConfigs | List of listenerConfigHolder | True | partition lost listener configurations | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the map to remain functional. When {@code null}, split brain protection does not apply to this map's operations. | 2.0 |
| mapStoreConfig | MapStoreConfigHolder | True | configuration of backing map store or {@code null} for none | 2.0 |
| nearCacheConfig | NearCacheConfigHolder | True | configuration of near cache or {@code null} for none | 2.0 |
| wanReplicationRef | WanReplicationRef | True | reference to an existing WAN replication configuration | 2.0 |
| indexConfigs | List of indexConfig | True | index configurations | 2.0 |
| attributeConfigs | List of attributeConfig | True | map attributes | 2.0 |
| queryCacheConfigs | List of queryCacheConfigHolder | True | configurations for query caches on this map | 2.0 |
| partitioningStrategyClassName | String | True | name of class implementing {@code com.hazelcast.core.PartitioningStrategy} or {@code null} | 2.0 |
| partitioningStrategyImplementation | Data | True | a serialized instance of a partitioning strategy | 2.0 |
| hotRestartConfig | HotRestartConfig | True | hot restart configuration | 2.0 |
| eventJournalConfig | EventJournalConfig | True | event journal configuration | 2.0 |
| merkleTreeConfig | MerkleTreeConfig | True | merkle tree configuration | 2.0 |
| metadataPolicy | int | False | metadata policy configuration for the supported data types. Valid values are {@code CREATE_ON_UPDATE} and {@code OFF} | 2.0 |
| perEntryStatsEnabled | boolean | False | {@code true} to enable entry level statistics for the entries of this map.  otherwise {@code false}. Default value is {@code false} | 2.2 |
| dataPersistenceConfig | DataPersistenceConfig | False | Data persistence configuration | 2.5 |
| tieredStoreConfig | TieredStoreConfig | False | Tiered-Store configuration | 2.5 |
| partitioningAttributeConfigs | List of partitioningAttributeConfig | True | List of attributes used for creating AttributePartitioningStrategy. | 2.6 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0c01

Header only response message, no message body exist.

#### 7.29.13. DynamicConfig.AddReliableTopicConfig
```
Adds a new reliable topic configuration to a running cluster.
If a reliable topic configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of reliable topic | 2.0 |
| listenerConfigs | List of listenerConfigHolder | True | message listener configurations | 2.0 |
| readBatchSize | int | False | maximum number of items to read in a batch. | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.0 |
| topicOverloadPolicy | String | False | policy to handle an overloaded topic. Available values are {@code DISCARD_OLDEST}, {@code DISCARD_NEWEST}, {@code BLOCK} and {@code ERROR}. | 2.0 |
| executor | Data | True | a serialized {@link java.util.concurrent.Executor} instance to use for executing message listeners or {@code null} | 2.0 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0d01

Header only response message, no message body exist.

#### 7.29.14. DynamicConfig.AddCacheConfig
```
Adds a new cache configuration to a running cluster.
If a cache configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | cache name | 2.0 |
| keyType | String | True | class name of key type | 2.0 |
| valueType | String | True | class name of value type | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.0 |
| managementEnabled | boolean | False | {@code true} to enable management interface on this cache or {@code false} | 2.0 |
| readThrough | boolean | False | {@code true} to enable read through from a {@code CacheLoader} | 2.0 |
| writeThrough | boolean | False | {@code true} to enable write through to a {@code CacheWriter} | 2.0 |
| cacheLoaderFactory | String | True | name of cache loader factory class, if one is configured | 2.0 |
| cacheWriterFactory | String | True | name of cache writer factory class, if one is configured | 2.0 |
| cacheLoader | String | True | Factory name of cache loader factory class, if one is configured | 2.0 |
| cacheWriter | String | True | Factory name of cache writer factory class, if one is configured | 2.0 |
| backupCount | int | False | number of synchronous backups | 2.0 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.0 |
| inMemoryFormat | String | False | data type used to store entries. Valid values are {@code BINARY}, {@code OBJECT} and {@code NATIVE}. | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the cache to remain functional. When {@code null}, split brain protection does not apply to this cache's operations. | 2.0 |
| mergePolicy | String | True | name of a class implementing SplitBrainMergePolicy that handles merging of values for this cache while recovering from network partitioning | 2.0 |
| mergeBatchSize | int | False | number of entries to be sent in a merge operation | 2.0 |
| disablePerEntryInvalidationEvents | boolean | False | when {@code true} disables invalidation events for per entry but full-flush invalidation events are still enabled. | 2.0 |
| partitionLostListenerConfigs | List of listenerConfigHolder | True | partition lost listener configurations | 2.0 |
| expiryPolicyFactoryClassName | String | True | expiry policy factory class name. When configuring an expiry policy, either this or {@ode timedExpiryPolicyFactoryConfig} should be configured. | 2.0 |
| timedExpiryPolicyFactoryConfig | TimedExpiryPolicyFactoryConfig | True | expiry policy factory with duration configuration | 2.0 |
| cacheEntryListeners | List of cacheSimpleEntryListenerConfig | True | cache entry listeners configuration | 2.0 |
| evictionConfig | EvictionConfigHolder | True | cache eviction configuration | 2.0 |
| wanReplicationRef | WanReplicationRef | True | reference to an existing WAN replication configuration | 2.0 |
| eventJournalConfig | EventJournalConfig | True | Event Journal configuration | 2.0 |
| hotRestartConfig | HotRestartConfig | True | hot restart configuration | 2.0 |
| merkleTreeConfig | MerkleTreeConfig | True | merkle tree configuration | 2.3 |
| dataPersistenceConfig | DataPersistenceConfig | False | Data persistence configuration | 2.5 |
| userCodeNamespace | String | True | Name of the User Code Namespace applied to this instance. | 2.7 |

#### Response Message
**Message Type:** 0x1b0e01

Header only response message, no message body exist.

#### 7.29.15. DynamicConfig.AddFlakeIdGeneratorConfig
```
Adds a new flake ID generator configuration to a running cluster.
If a flake ID generator configuration for the same name already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b0f00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of {@code FlakeIdGenerator} | 2.0 |
| prefetchCount | int | False | how many IDs are pre-fetched on the background when one call to {@code newId()} is made | 2.0 |
| prefetchValidity | long | False | for how long the pre-fetched IDs can be used | 2.0 |
| statisticsEnabled | boolean | False | {@code true} to enable gathering of statistics, otherwise {@code false} | 2.0 |
| nodeIdOffset | long | False | Offset that will be added to the node id assigned to the cluster members for this generator. | 2.0 |
| epochStart | long | False | offset of timestamp component in milliseconds  | 2.0 |
| bitsSequence | int | False | bit length of sequence component  | 2.0 |
| bitsNodeId | int | False | bit length of node id component | 2.0 |
| allowedFutureMillis | long | False | how far to the future is it allowed to go to generate IDs | 2.0 |

#### Response Message
**Message Type:** 0x1b0f01

Header only response message, no message body exist.

#### 7.29.16. DynamicConfig.AddPNCounterConfig
```
Adds a new CRDT PN counter configuration to a running cluster.
If a PN counter configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1b1000

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | name of the CRDT PN counter configuration | 2.0 |
| replicaCount | int | False | number of replicas on which the CRDT state is kept | 2.0 |
| statisticsEnabled | boolean | False | set to {@code true} to enable statistics on this multimap configuration | 2.0 |
| splitBrainProtectionName | String | True | name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the lock to remain functional. When {@code null}, split brain protection does not apply to this lock configuration's operations. | 2.0 |

#### Response Message
**Message Type:** 0x1b1001

Header only response message, no message body exist.

#### 7.29.17. DynamicConfig.AddDataConnectionConfig
```
Adds a data connection configuration.
If a data connection configuration with the given {@code name} already exists, then
the new configuration is ignored and the existing one is preserved.

```

**Available since:** 2.6

#### Request Message
**Message Type:** 0x1b1100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of this data connection, must be unique. | 2.6 |
| type | String | False | Type of the data connection as specified in the DataConnectionRegistration. | 2.6 |
| shared | boolean | False | {@code true} if an instance of the data connection will be shared.  Depending on the implementation of the data connection the shared instance may be  single a thread-safe instance, or not thread-safe, but a pooled instance.  {@code false} when on each usage a new instance of the underlying resource should be created. The default is {@code true}. | 2.6 |
| properties | Map of string to string | False | Properties of the data connection configuration. | 2.6 |

#### Response Message
**Message Type:** 0x1b1101

Header only response message, no message body exist.

#### 7.29.18. DynamicConfig.AddWanReplicationConfig
```
Adds a WAN replication configuration.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x1b1200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | WAN replication configuration name. | 2.7 |
| consumerConfig | WanConsumerConfigHolder | True | The WAN consumer configuration. | 2.7 |
| customPublisherConfigs | List of wanCustomPublisherConfigHolder | False | The WAN custom publisher configurations. | 2.7 |
| batchPublisherConfigs | List of wanBatchPublisherConfigHolder | False | The WAN batch publisher configurations. | 2.7 |

#### Response Message
**Message Type:** 0x1b1201

Header only response message, no message body exist.

#### 7.29.19. DynamicConfig.AddUserCodeNamespaceConfig
```
Adds a user code namespace configuration.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x1b1300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Namespace configuration name. | 2.7 |
| resources | List of resourceDefinition | False | List of resource definitions. | 2.7 |

#### Response Message
**Message Type:** 0x1b1301

Header only response message, no message body exist.

#### 7.29.20. DynamicConfig.AddVectorCollectionConfig
```
Adds a new vector collection configuration to a running cluster.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x1b1400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | vector collection name | 2.8 |
| indexConfigs | List of vectorIndexConfig | False | vector index configurations | 2.8 |
| backupCount | int | False | number of synchronous backups | 2.9 |
| asyncBackupCount | int | False | number of asynchronous backups | 2.9 |
| splitBrainProtectionName | String | True | Name of an existing configured split brain protection to be used to determine the minimum number of members required in the cluster for the VectorCollection to remain functional. When {@code null}, split brain protection does not apply to this VectorCollection's operations. | 2.9 |
| mergePolicy | String | False | Name of a class implementing SplitBrainMergePolicy that handles merging of values for this VectorCollection while recovering from network partitioning. | 2.9 |
| mergeBatchSize | int | False | Number of entries to be sent in a merge operation. | 2.9 |

#### Response Message
**Message Type:** 0x1b1401

Header only response message, no message body exist.

### 7.30. FlakeIdGenerator
**Service id:** 28

#### 7.30.1. FlakeIdGenerator.NewIdBatch
```
Fetches a new batch of ids for the given flake id generator.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1c0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the flake id generator. | 2.0 |
| batchSize | int | False | Number of ids that will be fetched on one call. | 2.0 |

#### Response Message
**Message Type:** 0x1c0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| base | long | False | First id in the batch. | 2.0 |
| increment | long | False | Increment for the next id in the batch. | 2.0 |
| batchSize | int | False | Number of ids in the batch. | 2.0 |

### 7.31. PNCounter
**Service id:** 29

#### 7.31.1. PNCounter.Get
```
Query operation to retrieve the current value of the PNCounter.
<p>
The invocation will return the replica timestamps (vector clock) which
can then be sent with the next invocation to keep session consistency
guarantees.
The target replica is determined by the {@code targetReplica} parameter.
If smart routing is disabled, the actual member processing the client
message may act as a proxy.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1d0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | the name of the PNCounter | 2.0 |
| replicaTimestamps | Map of uUID to long | False | last observed replica timestamps (vector clock) | 2.0 |
| targetReplicaUUID | UUID | False | the target replica | 2.0 |

#### Response Message
**Message Type:** 0x1d0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| value | long | False | Value of the counter. | 2.0 |
| replicaTimestamps | Map of uUID to long | False | last observed replica timestamps (vector clock) | 2.0 |
| replicaCount | int | False | Number of replicas that keep the state of this counter. | 2.0 |

#### 7.31.2. PNCounter.Add
```
Adds a delta to the PNCounter value. The delta may be negative for a
subtraction.
<p>
The invocation will return the replica timestamps (vector clock) which
can then be sent with the next invocation to keep session consistency
guarantees.
The target replica is determined by the {@code targetReplica} parameter.
If smart routing is disabled, the actual member processing the client
message may act as a proxy.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1d0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | the name of the PNCounter | 2.0 |
| delta | long | False | the delta to add to the counter value, can be negative | 2.0 |
| getBeforeUpdate | boolean | False | {@code true} if the operation should return the counter value before the addition, {@code false} if it should return the value after the addition | 2.0 |
| replicaTimestamps | Map of uUID to long | False | last observed replica timestamps (vector clock) | 2.0 |
| targetReplicaUUID | UUID | False | the target replica | 2.0 |

#### Response Message
**Message Type:** 0x1d0201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| value | long | False | Value of the counter. | 2.0 |
| replicaTimestamps | Map of uUID to long | False | last observed replica timestamps (vector clock) | 2.0 |
| replicaCount | int | False | Number of replicas that keep the state of this counter. | 2.0 |

#### 7.31.3. PNCounter.GetConfiguredReplicaCount
```
Returns the configured number of CRDT replicas for the PN counter with
the given {@code name}.
The actual replica count may be less, depending on the number of data
members in the cluster (members that own data).

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1d0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | the name of the PNCounter | 2.0 |

#### Response Message
**Message Type:** 0x1d0301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False | the configured replica count | 2.0 |

### 7.32. CPGroup
**Service id:** 30

#### 7.32.1. CPGroup.CreateCPGroup
```
Creates a new CP group with the given name

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1e0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| proxyName | String | False | The proxy name of this data structure instance | 2.0 |

#### Response Message
**Message Type:** 0x1e0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | ID of the CP group that contains the CP object | 2.0 |

#### 7.32.2. CPGroup.DestroyCPObject
```
Destroys the distributed object with the given name on the requested
CP group

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1e0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group id of this distributed object | 2.0 |
| serviceName | String | False | The service of this distributed object | 2.0 |
| objectName | String | False | The name of this distributed object | 2.0 |

#### Response Message
**Message Type:** 0x1e0201

Header only response message, no message body exist.

### 7.33. CPSession
**Service id:** 31

#### 7.33.1. CPSession.CreateSession
```
Creates a session for the caller on the given CP group.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1f0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | ID of the CP group | 2.0 |
| endpointName | String | False | Name of the caller HazelcastInstance | 2.0 |

#### Response Message
**Message Type:** 0x1f0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| sessionId | long | False | Id of the session. | 2.0 |
| ttlMillis | long | False | Time to live value in milliseconds that must be respected by the caller. | 2.0 |
| heartbeatMillis | long | False | Time between heartbeats in milliseconds that must be respected by the caller. | 2.0 |

#### 7.33.2. CPSession.CloseSession
```
Closes the given session on the given CP group

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1f0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | ID of the CP group | 2.0 |
| sessionId | long | False | ID of the session | 2.0 |

#### Response Message
**Message Type:** 0x1f0201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | true if the session is found & closed, false otherwise. | 2.0 |

#### 7.33.3. CPSession.HeartbeatSession
```
Commits a heartbeat for the given session on the given cP group and
extends its session expiration time.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1f0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | ID of the CP group | 2.0 |
| sessionId | long | False | ID of the session | 2.0 |

#### Response Message
**Message Type:** 0x1f0301

Header only response message, no message body exist.

#### 7.33.4. CPSession.GenerateThreadId
```
Generates a new ID for the caller thread. The ID is unique in the given
CP group.

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0x1f0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | ID of the CP group | 2.0 |

#### Response Message
**Message Type:** 0x1f0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | A unique ID for the caller thread | 2.0 |

### 7.34. Sql
**Service id:** 33

#### 7.34.1. Sql.Execute_reserved
```
THIS MESSAGE IS NO LONGER USED BUT KEPT FOR BACKWARD COMPATIBILITY TESTS
Starts execution of an SQL query.

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x210100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| sql | String | False | Query string. | 2.1 |
| parameters | List of data | False | Query parameters. | 2.1 |
| timeoutMillis | long | False | Timeout in milliseconds. | 2.1 |
| cursorBufferSize | int | False | Cursor buffer size. | 2.1 |

#### Response Message
**Message Type:** 0x210101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| queryId | SqlQueryId | True | Query ID. | 2.1 |
| rowMetadata | List of sqlColumnMetadata | True | Row metadata. | 2.1 |
| rowPage | List of listCN_Data | True | Row page. | 2.1 |
| rowPageLast | boolean | False | Whether the row page is the last. | 2.1 |
| updateCount | long | False | The number of updated rows. | 2.1 |
| error | SqlError | True | Error object. | 2.1 |

#### 7.34.2. Sql.Fetch_reserved
```
Fetches the next row page.

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x210200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| queryId | SqlQueryId | False | Query ID. | 2.1 |
| cursorBufferSize | int | False | Cursor buffer size. | 2.1 |

#### Response Message
**Message Type:** 0x210201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| rowPage | List of listCN_Data | True | Row page. | 2.1 |
| rowPageLast | boolean | False | Whether the row page is the last. | 2.1 |
| error | SqlError | True | Error object. | 2.1 |

#### 7.34.3. Sql.Close
```
Closes server-side query cursor.

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x210300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| queryId | SqlQueryId | False | Query ID. | 2.1 |

#### Response Message
**Message Type:** 0x210301

Header only response message, no message body exist.

#### 7.34.4. Sql.Execute
```
Starts execution of an SQL query (as of 4.2).

```

**Available since:** 2.2

#### Request Message
**Message Type:** 0x210400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| sql | String | False | Query string. | 2.2 |
| parameters | List of data | False | Query parameters. | 2.2 |
| timeoutMillis | long | False | Timeout in milliseconds. | 2.2 |
| cursorBufferSize | int | False | Cursor buffer size. | 2.2 |
| schema | String | True | Schema name. | 2.2 |
| expectedResultType | byte | False | The expected result type. Possible values are:   ANY(0)   ROWS(1)   UPDATE_COUNT(2) | 2.2 |
| queryId | SqlQueryId | False | Query ID. | 2.2 |
| skipUpdateStatistics | boolean | False | Flag to skip updating phone home statistics. | 2.3 |

#### Response Message
**Message Type:** 0x210401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| rowMetadata | List of sqlColumnMetadata | True | Row metadata. | 2.2 |
| rowPage | SqlPage | True | Row page. | 2.2 |
| updateCount | long | False | The number of updated rows. | 2.2 |
| error | SqlError | True | Error object. | 2.2 |
| isInfiniteRows | boolean | False | Is the result set unbounded. | 2.5 |
| partitionArgumentIndex | int | False | Index of the partition-determining argument, -1 if not applicable. | 2.6 |

#### 7.34.5. Sql.Fetch
```
Fetches the next row page.

```

**Available since:** 2.2

#### Request Message
**Message Type:** 0x210500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| queryId | SqlQueryId | False | Query ID. | 2.2 |
| cursorBufferSize | int | False | Cursor buffer size. | 2.2 |

#### Response Message
**Message Type:** 0x210501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| rowPage | SqlPage | True | Row page. | 2.2 |
| error | SqlError | True | Error object. | 2.2 |

#### 7.34.6. Sql.MappingDdl
```
Derives CREATE MAPPING SQL.

```

**Available since:** 2.3

#### Request Message
**Message Type:** 0x210600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Object name to derive CREATE MAPPING SQL for. | 2.3 |

#### Response Message
**Message Type:** 0x210601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| sql | String | True | CREATE MAPPING SQL. | 2.3 |

### 7.35. CPSubsystem
**Service id:** 34

#### 7.35.1. CPSubsystem.AddMembershipListener
```
Registers a new CP membership listener.

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x220100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| local | boolean | False | Denotes whether register a local listener or not. | 2.1 |

#### Response Message
**Message Type:** 0x220101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Registration id for the listener. | 2.1 |

#### Event Message

##### MembershipEvent
**Message Type:** 0x220103

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| member | CPMember | False | Member which is added or removed. | 2.1 |
| type | byte | False | Type of the event. It is either ADDED(1) or REMOVED(2). | 2.1 |

#### 7.35.2. CPSubsystem.RemoveMembershipListener
```
Deregisters CP membership listener.

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x220200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| registrationId | UUID | False | The id of the listener which was provided during registration. | 2.1 |

#### Response Message
**Message Type:** 0x220201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if unregistered, false otherwise. | 2.1 |

#### 7.35.3. CPSubsystem.AddGroupAvailabilityListener
```
Registers a new CP group availability listener.

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x220300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| local | boolean | False | Denotes whether register a local listener or not. | 2.1 |

#### Response Message
**Message Type:** 0x220301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | False | Registration id for the listener. | 2.1 |

#### Event Message

##### GroupAvailabilityEvent
**Message Type:** 0x220303

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | Group id whose availability is reported. | 2.1 |
| members | List of cPMember | False | All members. | 2.1 |
| unavailableMembers | List of cPMember | False | Missing members. | 2.1 |
| isShutdown | boolean | False | Determines if the availability event is due to an explicit shutdown. | 2.7 |

#### 7.35.4. CPSubsystem.RemoveGroupAvailabilityListener
```
Deregisters CP availability listener.

```

**Available since:** 2.1

#### Request Message
**Message Type:** 0x220400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| registrationId | UUID | False | The id of the listener which was provided during registration. | 2.1 |

#### Response Message
**Message Type:** 0x220401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if unregistered, false otherwise. | 2.1 |

#### 7.35.5. CPSubsystem.GetCPGroupIds
```
Returns all the active CP group ids in the cluster. This is mainly used by a client side CPSubsystem because it does not 
have a RaftService.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x220500

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0x220501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of raftGroupId | False | List of active CP group ids. | 2.7 |

#### 7.35.6. CPSubsystem.GetCPObjectInfos
```
Returns all active CP structures that belong to the group with the provided CPGroupId and service name.
A snapshot is used to retrieve the result.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x220600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | Defines the cp group to return cp structures from | 2.7 |
| serviceName | String | False | The service name of the cp structures to return | 2.7 |
| tombstone | boolean | False | Whether to return cp tombstones. If true, only tombstones will be returned. If false,  only non-tombstone cp structures will be returned. | 2.7 |

#### Response Message
**Message Type:** 0x220601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of string | False | List of names of CP structures that belong to the specified cp group and service. | 2.7 |

### 7.36. CPMap
**Service id:** 35

#### 7.36.1. CPMap.Get
```
Gets the value associated with the key in the specified map.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x230100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group ID of this CPMap instance. | 2.7 |
| name | String | False | Name of this CPMap instance. | 2.7 |
| key | Data | False | Key of the value to retrieve. | 2.7 |

#### Response Message
**Message Type:** 0x230101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the map lookup.  | 2.7 |

#### 7.36.2. CPMap.Put
```
Puts the key-value into the specified map.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x230200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group ID of this CPMap instance. | 2.7 |
| name | String | False | Name of this CPMap instance. | 2.7 |
| key | Data | False | Key of the value. | 2.7 |
| value | Data | False | Value to associate with the key. | 2.7 |

#### Response Message
**Message Type:** 0x230201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | Previous value associated with the key.  | 2.7 |

#### 7.36.3. CPMap.Set
```
Sets the key-value in the specified map.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x230300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group ID of this CPMap instance. | 2.7 |
| name | String | False | Name of this CPMap instance. | 2.7 |
| key | Data | False | Key of the value. | 2.7 |
| value | Data | False | Value to associate with the key. | 2.7 |

#### Response Message
**Message Type:** 0x230301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | Always null, set does not return any previous value. | 2.7 |

#### 7.36.4. CPMap.Remove
```
Removes the value associated with the key in the specified map.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x230400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group ID of this CPMap instance. | 2.7 |
| name | String | False | Name of this CPMap instance. | 2.7 |
| key | Data | False | Key of the value to remove. | 2.7 |

#### Response Message
**Message Type:** 0x230401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | The result of the remove.  | 2.7 |

#### 7.36.5. CPMap.Delete
```
Deletes the value associated with the key in the specified map.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x230500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group ID of this CPMap instance. | 2.7 |
| name | String | False | Name of this CPMap instance. | 2.7 |
| key | Data | False | Key of the value to delete. | 2.7 |

#### Response Message
**Message Type:** 0x230501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | Always null, delete does not return any value. | 2.7 |

#### 7.36.6. CPMap.CompareAndSet
```
Tests if the value associated with the key is expectedValue and if so associates key with
newValue.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x230600

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group ID of this CPMap instance. | 2.7 |
| name | String | False | Name of this CPMap instance. | 2.7 |
| key | Data | False | Key of the data that is subject of the compare and set. | 2.7 |
| expectedValue | Data | False | The expected value associated with key. | 2.7 |
| newValue | Data | False | The new value to associate with key. | 2.7 |

#### Response Message
**Message Type:** 0x230601

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if key was associated with newValue, otherwise false. | 2.7 |

#### 7.36.7. CPMap.PutIfAbsent
```
Puts the key-value into the specified map if the key is not currently associated with a value.

```

**Available since:** 2.7

#### Request Message
**Message Type:** 0x230700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| groupId | RaftGroupId | False | CP group ID of this CPMap instance. | 2.7 |
| name | String | False | Name of this CPMap instance. | 2.7 |
| key | Data | False | Key of the value. | 2.7 |
| value | Data | False | Value to associate with the key. | 2.7 |

#### Response Message
**Message Type:** 0x230701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | True | Value associated with the key if already present, otherwise null. | 2.7 |

### 7.37. VectorCollection
**Service id:** 36

#### 7.37.1. VectorCollection.Put
```
Puts a document into the Vector Collection.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240100

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |
| key | Data | False | Key for the document. | 2.8 |
| value | VectorDocument | False | Value for the entry. | 2.8 |

#### Response Message
**Message Type:** 0x240101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| value | VectorDocument | True | Value previously associated with the key if any. | 2.8 |

#### 7.37.2. VectorCollection.PutIfAbsent
```
Puts an entry into this map if the specified key is not already associated with a value.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240200

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |
| key | Data | False | Key for the document. | 2.8 |
| value | VectorDocument | False | Value for the entry. | 2.8 |

#### Response Message
**Message Type:** 0x240201

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| value | VectorDocument | True | Value previously associated with the key if any. | 2.8 |

#### 7.37.3. VectorCollection.PutAll
```
The effect of this call is equivalent to set(k, v) on this VectorCollection once for each mapping from key k to value v.
The behavior of this operation is undefined if the specified collection is modified while the operation is in progress.
Note that all keys in the request should belong to the partition ID to which this request is being sent.
Any key that matches to a different partition ID shall be ignored.
The API implementation using this request may need to send multiple of these request messages for different partitions.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240300

**Partition Identifier:** Murmur hash of any key belongs to target partition % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |
| entries | Map of data to vectorDocument | False | Key/VectorDocument entries to be stored in this VectorCollection. | 2.8 |

#### Response Message
**Message Type:** 0x240301

Header only response message, no message body exist.

#### 7.37.4. VectorCollection.Get
```
Returns the VectorDocument for the given key.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240400

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |
| key | Data | False | Key for the document. | 2.8 |

#### Response Message
**Message Type:** 0x240401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| value | VectorDocument | True | The value for the key if it exists. | 2.8 |

#### 7.37.5. VectorCollection.Remove
```
Removes the mapping for a key from this VectorCollection.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240500

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the VectorCollection. | 2.8 |
| key | Data | False | Key for the entry. | 2.8 |

#### Response Message
**Message Type:** 0x240501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| value | VectorDocument | True | Value previously associated with the key if any. | 2.8 |

#### 7.37.6. VectorCollection.Set
```
Puts a document into the Vector Collection without returning previous value.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240600

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |
| key | Data | False | Key for the document. | 2.8 |
| value | VectorDocument | False | Value for the entry. | 2.8 |

#### Response Message
**Message Type:** 0x240601

Header only response message, no message body exist.

#### 7.37.7. VectorCollection.Delete
```
Removes the mapping for a key from this VectorCollection without returning previous value.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240700

**Partition Identifier:** Murmur hash of key % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the VectorCollection. | 2.8 |
| key | Data | False | Key for the entry. | 2.8 |

#### Response Message
**Message Type:** 0x240701

Header only response message, no message body exist.

#### 7.37.8. VectorCollection.SearchNearVector
```
Returns the VectorDocuments closest to the given vector.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240800

**Partition Identifier:** Murmur hash of none % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |
| vectors | List of vectorPair | False | Vector for which closest neighbours should be returned. | 2.8 |
| options | VectorSearchOptions | False | Search options. | 2.8 |

#### Response Message
**Message Type:** 0x240801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| result | List of vectorSearchResult | False | Zero or more VectorSearchResult values. | 2.8 |

#### 7.37.9. VectorCollection.Optimize
```
Optimize index.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240900

**Partition Identifier:** Murmur hash of none % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |
| indexName | String | True | Name of the Index to optimize. A null value triggers the optimization of the only index within the collection. | 2.8 |
| uuid | UUID | True | UUID of this optimization request. | 2.9 |

#### Response Message
**Message Type:** 0x240901

Header only response message, no message body exist.

#### 7.37.10. VectorCollection.Clear
```
Clear vector collection.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240a00

**Partition Identifier:** Murmur hash of none % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |

#### Response Message
**Message Type:** 0x240a01

Header only response message, no message body exist.

#### 7.37.11. VectorCollection.Size
```
Size of vector collection.

```

**Available since:** 2.8

#### Request Message
**Message Type:** 0x240b00

**Partition Identifier:** Murmur hash of none % `PARTITION_COUNT`

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| name | String | False | Name of the Vector Collection. | 2.8 |

#### Response Message
**Message Type:** 0x240b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False | the number of entries in this collection | 2.8 |

### 7.38. Experimental
**Service id:** 253

#### 7.38.1. Experimental.PipelineSubmit
```
The message is used to transfer the declarative pipeline definition and the related resource files from client to the server.
```

**Available since:** 2.7

#### Request Message
**Message Type:** 0xfd0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobName | String | True | The name of the submitted Job using this pipeline. | 2.7 |
| pipelineDefinition | String | False | The definition of the pipeline steps. It currently uses the YAML format. | 2.7 |
| resourceBundle | byteArray | True | This is the zipped file which contains the user project folders and files. For Python project, it is the Python project files. It is optional in the sense that if the user likes to use a user docker image with all the resources and project files included, this parameter can be null. | 2.7 |
| resourceBundleChecksum | int | False | This is the CRC32 checksum over the resource bundle bytes. | 2.7 |

#### Response Message
**Message Type:** 0xfd0101

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False | This is the unique identifier for the job which is created for this pipeline | 2.7 |

### 7.39. Jet
**Service id:** 254

#### 7.39.1. Jet.SubmitJob
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |
| dag | Data | False |  | 2.0 |
| jobConfig | Data | True |  | 2.0 |
| lightJobCoordinator | UUID | True |  | 2.3 |

#### Response Message
**Message Type:** 0xfe0101

Header only response message, no message body exist.

#### 7.39.2. Jet.TerminateJob
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |
| terminateMode | int | False |  | 2.0 |
| lightJobCoordinator | UUID | True |  | 2.3 |

#### Response Message
**Message Type:** 0xfe0201

Header only response message, no message body exist.

#### 7.39.3. Jet.GetJobStatus
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |

#### Response Message
**Message Type:** 0xfe0301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | int | False |  | 2.0 |

#### 7.39.4. Jet.GetJobIds
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| onlyName | String | True |  | 2.3 |
| onlyJobId | long | False |  | 2.3 |

#### Response Message
**Message Type:** 0xfe0401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | False |  | 2.3 |

#### 7.39.5. Jet.JoinSubmittedJob
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |
| lightJobCoordinator | UUID | True |  | 2.3 |

#### Response Message
**Message Type:** 0xfe0501

Header only response message, no message body exist.

#### 7.39.7. Jet.GetJobSubmissionTime
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0700

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |
| lightJobCoordinator | UUID | True |  | 2.3 |

#### Response Message
**Message Type:** 0xfe0701

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | long | False |  | 2.0 |

#### 7.39.8. Jet.GetJobConfig
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0800

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |
| lightJobCoordinator | UUID | True |  | 2.4 |

#### Response Message
**Message Type:** 0xfe0801

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | False |  | 2.0 |

#### 7.39.9. Jet.ResumeJob
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0900

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |

#### Response Message
**Message Type:** 0xfe0901

Header only response message, no message body exist.

#### 7.39.10. Jet.ExportSnapshot
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0a00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |
| name | String | False |  | 2.0 |
| cancelJob | boolean | False |  | 2.0 |

#### Response Message
**Message Type:** 0xfe0a01

Header only response message, no message body exist.

#### 7.39.11. Jet.GetJobSummaryList
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0b00

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0xfe0b01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | False |  | 2.0 |

#### 7.39.12. Jet.ExistsDistributedObject
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0c00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| serviceName | String | False |  | 2.0 |
| objectName | String | False |  | 2.0 |

#### Response Message
**Message Type:** 0xfe0c01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False |  | 2.0 |

#### 7.39.13. Jet.GetJobMetrics
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0d00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |

#### Response Message
**Message Type:** 0xfe0d01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | False |  | 2.0 |

#### 7.39.14. Jet.GetJobSuspensionCause
```

```

**Available since:** 2.0

#### Request Message
**Message Type:** 0xfe0e00

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.0 |

#### Response Message
**Message Type:** 0xfe0e01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | Data | False |  | 2.0 |

#### 7.39.15. Jet.GetJobAndSqlSummaryList
```

```

**Available since:** 2.5

#### Request Message
**Message Type:** 0xfe0f00

Header only request message, no message body exist.

#### Response Message
**Message Type:** 0xfe0f01

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | List of jobAndSqlSummary | False |  | 2.5 |

#### 7.39.16. Jet.IsJobUserCancelled
```

```

**Available since:** 2.6

#### Request Message
**Message Type:** 0xfe1000

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.6 |

#### Response Message
**Message Type:** 0xfe1001

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False |  | 2.6 |

#### 7.39.17. Jet.UploadJobMetaData
```

```

**Available since:** 2.6

#### Request Message
**Message Type:** 0xfe1100

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| sessionId | UUID | False | Unique session ID of the job upload request | 2.6 |
| jarOnMember | boolean | False | Flag that indicates that the jar to be executed is already present on the member, and no jar will be uploaded from the client | 2.6 |
| fileName | String | False | Name of the jar file without extension | 2.6 |
| sha256Hex | String | False | Hexadecimal SHA256 of the jar file | 2.6 |
| snapshotName | String | True | Name of the initial snapshot to start the job from | 2.6 |
| jobName | String | True | Name of the job | 2.6 |
| mainClass | String | True | Fully qualified name of the main class inside the JAR file | 2.6 |
| jobParameters | List of string | False | Arguments to pass to the supplied jar file | 2.6 |

#### Response Message
**Message Type:** 0xfe1101

Header only response message, no message body exist.

#### 7.39.18. Jet.UploadJobMultipart
```

```

**Available since:** 2.6

#### Request Message
**Message Type:** 0xfe1200

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| sessionId | UUID | False | Unique session ID of the job upload request | 2.6 |
| currentPartNumber | int | False | The current part number being sent. Starts from 1 | 2.6 |
| totalPartNumber | int | False | The total number of parts to be sent. Minimum value is 1 | 2.6 |
| partData | byteArray | False | The binary data of the message part | 2.6 |
| partSize | int | False | The size of binary data | 2.6 |
| sha256Hex | String | False | Hexadecimal SHA256 of the message part | 2.6 |

#### Response Message
**Message Type:** 0xfe1201

Header only response message, no message body exist.

#### 7.39.19. Jet.AddJobStatusListener
```
Adds a JobStatusListener to the specified job.

```

**Available since:** 2.6

#### Request Message
**Message Type:** 0xfe1300

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False | ID of job. | 2.6 |
| lightJobCoordinator | UUID | True | Address of the job coordinator for light jobs, null otherwise. | 2.6 |
| localOnly | boolean | False | If true fires events that originated from this node only, otherwise fires all events. | 2.6 |

#### Response Message
**Message Type:** 0xfe1301

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | UUID | True | A unique registration ID which is used as a key to remove the listener. | 2.6 |

#### Event Message

##### JobStatus
**Message Type:** 0xfe1303

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False | ID of job. | 2.6 |
| previousStatus | int | False | NOT_RUNNING(0) STARTING(1) RUNNING(2) SUSPENDED(3) SUSPENDED_EXPORTING_SNAPSHOT(4) | 2.6 |
| newStatus | int | False | NOT_RUNNING(0) STARTING(1) RUNNING(2) SUSPENDED(3) SUSPENDED_EXPORTING_SNAPSHOT(4) FAILED(6) COMPLETED(7) | 2.6 |
| description | String | True | If the event is generated by the user, indicates the action; if there is a failure, indicates the cause; otherwise, null. | 2.6 |
| userRequested | boolean | False | Indicates whether the event is generated by the user via {@code Job.suspend()}, {@code Job.resume()}, {@code Job.restart()}, {@code Job.cancel()}, {@code Job.exportSnapshot(String)} or {@code Job.cancelAndExportSnapshot(String)}. | 2.6 |

#### 7.39.20. Jet.RemoveJobStatusListener
```
Removes the specified job status listener. If there is no such listener
added before, this call does no change in the cluster and returns false.

```

**Available since:** 2.6

#### Request Message
**Message Type:** 0xfe1400

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False | ID of job. | 2.6 |
| registrationId | UUID | False | ID of registered listener. | 2.6 |

#### Response Message
**Message Type:** 0xfe1401

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| response | boolean | False | True if registration is removed, false otherwise. | 2.6 |

#### 7.39.21. Jet.UpdateJobConfig
```

```

**Available since:** 2.6

#### Request Message
**Message Type:** 0xfe1500

**Partition Identifier:** `-1`


| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| jobId | long | False |  | 2.6 |
| deltaConfig | Data | False |  | 2.6 |

#### Response Message
**Message Type:** 0xfe1501

| Name | Type | Nullable | Description | Available Since |
| ---- | ---- | -------- | ----------- | --------------- |
| updatedConfig | Data | False |  | 2.6 |

## 8. Copyright

Copyright (c) 2008-2024, Hazelcast, Inc. All Rights Reserved.

Visit [www.hazelcast.com](https://hazelcast.com/) for more info.