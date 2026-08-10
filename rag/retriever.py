from math import sqrt
from rag.schema import Chunk
from rag.vector_store import InMemoryVectorStore


class Retriever:
    def __init__(self, store):
        self.store = store

    def retrieve(self, queryEmbedding: list[float], top_k: int = 5):
        scored_chunks = []

        for chunk in self.store.get_chunks():
            if chunk.embedding is None:
                continue

            score = self.cosine_similarity(queryEmbedding, chunk.embedding)
            scored_chunks.append((chunk, score))

        scored_chunks.sort(key=lambda item:item[1], reverse=True)

        return [chunk for chunk, _ in scored_chunks[:top_k]]

    def cosine_similarity(self, vector1: list[float], vector2: list[float]) -> float:
        dot_product = 0.0

        dot_product = 0.0

        for a, b in zip(vector1, vector2):
            dot_product += a * b

        magnitude1 = 0.0
        magnitude2 = 0.0

        for value in vector1:
            magnitude1 += value * value

        for value in vector2:
            magnitude2 += value * value

        magnitude1 = sqrt(magnitude1)
        magnitude2 = sqrt(magnitude2)

        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        return dot_product / (magnitude1 * magnitude2)

        """"
===============================================================================
KODUN ÖZETİ VE MİMARİ ANLAMI
===============================================================================

1. BU KOD NEDİR? (Ne İşe Yarar?)
---------------------------------
- Bu kod, bir RAG (Retrieval-Augmented Generation) sisteminin "Bilgi Getirici" 
  (Retriever) bileşenidir.
- Bellekte duran (InMemoryVectorStore) metin parçalarının (Chunk) vektörlerini tarar.
- Kullanıcının attığı sorgu vektörü (`query_embedding`) ile sistemdeki tüm chunk'ların
  vektörlerini karşılaştırarak anlamsal olarak en yakın `top_k` adet (varsayılan: 5)
  metin parçasını bulup getirir.


2. BU KODDAN NE ANLAMALISINIZ? (Temel Çıkarımlar)
--------------------------------------------------
- **Anlamsal Arama (Semantic Search) Mantığı:**
  Sistem klasik kelime eşleşmesi (keyword search) yapmaz. Metinlerin yapay zeka
  tarafından oluşturulmuş sayı dizilerini (embedding) karşılaştırarak anlamca
  birbirine ne kadar benzediğini ölçer.

- **Saf Python İle Vektör Matematiği (Cosine Similarity):**
  `cosine_similarity` metodu, hiçbir dış kütüphane (NumPy, PyTorch vb.) kullanmadan
  iki vektör arasındaki açının kosinüsünü manuel hesaplar:
    * `dot_product`: İki vektörün iç çarpımı (yönsel benzerliği).
    * `magnitude`: Vektörlerin uzunlukları/büyüklükleri (L2 normu).
    * Sonuç: `dot_product / (magnitude1 * magnitude2)` formülü ile iki vektörün
      yönsel olarak ne kadar aynı doğrultuda olduğunu -1 ile 1 arasında ölçer.

- **Veri Doğrulama ve Filtreleme:**
  `if chunk.embedding is None` kontrolü ile vektörize edilmemiş (bozuk veya eksik)
  metin parçaları hesaplamaya dahil edilmeden atlanır.

- **Prototip / Eğitim Amaçlı Yapı (Performance Context):**
  * Bu kod, vektör arama mantığını anlamak için yazılmış saf bir Python simülasyonudur.
  * Tüm chunk'lar üzerinde `for` döngüsü ile tek tek gezdiği için (O(N) zaman karmaşıklığı)
    binlerce/milyonlarca doküman olduğunda yavaş çalışacaktır.
  * Gerçek üretim (Production) ortamlarında bu işlem saf Python döngüsü yerine
    FAISS, Qdrant, ChromaDB veya Pgvector gibi C++/GPU tabanlı vektör veritabanlarına
    yaptırılır.
===============================================================================
"""