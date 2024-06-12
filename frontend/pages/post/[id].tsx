import { GetStaticPaths, GetStaticProps } from 'next';
import axiosInstance from '../../utils/axiosInstance';

interface Post {
  userId: number;
  id: number;
  title: string;
  body: string;
}

type PostProps = {
  post: Post;
};

const PostPage: React.FC<PostProps> = ({ post }) => (
  <div>
    <h1>{post.title}</h1>
    <p>{post.body}</p>
  </div>
);

export const getStaticPaths: GetStaticPaths = async () => {
  const { data: posts } = await axiosInstance.get('/posts');
  const paths = posts.map((post: Post) => ({ params: { id: post.id.toString() } }));
  return { paths, fallback: false };
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const { data: post } = await axiosInstance.get(`/posts/${params?.id}`);
  return { props: { post } };
};

export default PostPage;
